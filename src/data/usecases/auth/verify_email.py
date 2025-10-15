from src.domain.usecases.auth.verify_email import VerifyEmailUseCase
from src.data.interfaces.auth_cahce_interface import AuthCacheInterface
from src.data.interfaces.auth_interface import AuthRepositoryInterface
from src.data.interfaces.stmp_service_interface import SMTPServiceInterface
from src.data.interfaces.urSafeTokenService_interface import URSafeTokenServiceInterface
from src.data.interfaces.jwt_service_interface import JWTServiceInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.InvalidToken import InvalidToken
from src.errors.types.ExpiredToken import ExpiredToken
from src.errors.types.ErrorCache import ErrorCache
from src.domain.models.user_email import UserEmail
import re
class VerifyEmailUseCaseImpl(VerifyEmailUseCase):
    def __init__(self,auth_repository:AuthRepositoryInterface,auth_cache:AuthCacheInterface,email_service:SMTPServiceInterface,token_service:URSafeTokenServiceInterface,jwt_service:JWTServiceInterface):
        self.auth_repository = auth_repository
        self.auth_cache = auth_cache
        self.email_service = email_service
        self.token_service = token_service
        self.jwt_service = jwt_service
        self.key = None
        self.token = None
        self.userId = None
        self.nome = None
    def verify(self, email:str, token:str):
        self.__validate_email(email=email)
        self.__validate_token(token=token)
        self.__verify_token()
        self.__create_user()
        self.__delete_token()
        self.__create_token_access()
        self.__send_welcome_email(email=email)
        return self.__format_response() 
    def __validate_email(self,email:str)-> None:
        if len(email) > 100 or not email or re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
            raise HttpBadRequestError("Email inválido")
    def __validate_token(self,token:str)-> None:
        if not token or len(token) > 255:
            raise HttpBadRequestError("Token inválido")
        self.key = f"verify_email:{token}"
    def __verify_token(self)-> None:
        user_data =  self.auth_cache.get_temp_token(key=self.key)
        if not user_data:
            raise ExpiredToken("Token expirado ou inválido")
    def __create_user(self)->None:
        user_data = self.auth_cache.get_temp_token(key=self.key)
        if not user_data:
            raise ExpiredToken("Token expirado ou inválido")
        self.auth_repository.create_user(user_data=user_data)
        user = self.auth_repository.get_user_by_email(email=user_data['email'])
        # user.is_verified = True
        if not user:
            raise InvalidToken("Usuário não encontrado")
        self.userId = user.id
        self.nome = user.nome
    def __delete_token(self)->None:
        delete = self.auth_cache.delete_temp_token(key=self.key)
        if delete == False:
            raise ErrorCache("Erro ao deletar token do cache")
    def __create_token_access(self) -> None:
        self.token = self.jwt_service.create_access_token(
            user_id=self.userId
        )
    def __send_welcome_email(self,email:str)->None:
        email_send = UserEmail(
            email=email,
            name=self.nome
        )
        self.email_service.send_welcome_email(email=email_send)
    def __format_response(self):
        user = self.auth_repository.get_user_by_id(user_id=self.userId)
        response = {
            "success":True,
            "message":"Email verificado com sucesso",
            "user":{
                "id":user.id,
                "nome":user.nome,
                "email":user.email,
                "role":user.role,
                "is_verified":user.is_verified
            },
            "access_token":self.token
        }
        return response