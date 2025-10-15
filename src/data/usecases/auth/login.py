from src.domain.usecases.auth.login import LoginUseCase 
from typing import Dict
from src.domain.models.auth_model import AuthModel
from src.data.interfaces.auth_cahce_interface import AuthCacheInterface
from src.data.interfaces.auth_interface import AuthRepositoryInterface 
from src.data.interfaces.jwt_service_interface import JWTServiceInterface
from src.data.interfaces.stmp_service_interface import SMTPServiceInterface
from src.data.interfaces.password_service_interface import PasswordServiceInterface
from src.errors.types.InvalidCredentiais import InvalidCredentialsError
from src.data.interfaces.urSafeTokenService_interface import URSafeTokenServiceInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.UserAlreadyExists import UserAlreadyExists
from src.errors.types.AccountIsNotVerified import AccountIsNotVerified
from src.errors.types.http_not_found import HttpNotFoundError
from datetime import datetime,timedelta
import re 
class LoginUseCaseImpl(LoginUseCase):
    def __init__(self, auth_repository: AuthRepositoryInterface, auth_cache: AuthCacheInterface, jwt_service: JWTServiceInterface, smtp_service: SMTPServiceInterface, password_service: PasswordServiceInterface, ur_safe_token_service: URSafeTokenServiceInterface):
        self.auth_repository = auth_repository
        self.auth_cache = auth_cache
        self.jwt_service = jwt_service
        self.smtp_service = smtp_service
        self.password_service = password_service
        self.ur_safe_token_service = ur_safe_token_service 
        self.user = None
        self.refresh_token = None
        self.access_token = None
    def login(self, email:str, senha:str)->Dict:
        self.__validate_data(email=email, senha=senha)
        self.__validate_user(email=email)
        self.__validate_password(senha=senha)
        self.__generate_tokens()
        return self.__format_response() 
    def __validate_data(self,email:str,senha:str)->None:
        if not email or re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
            raise HttpBadRequestError("Email inválido")
        if not senha or len(senha) < 6:
            raise HttpBadRequestError("Senha inválida, deve conter no mínimo 6 caracteres")
    def __validate_user(self,email:str)-> None:
        user = self.auth_repository.get_user_by_email(
            email=email
        )
        if not user:
            raise HttpNotFoundError("Usuário não encontrado")
        self.user = user
        if user.is_verified == False:
            raise AccountIsNotVerified("usuario não verificado")
    def __validate_password(self,senha:str)->None:
        password_is_valid = self.password_service.verify_password(
            hashed_password=self.user.senha,
            password=senha
        )
        if password_is_valid == False:
            raise HttpBadRequestError("Senha inválida")
    def __generate_tokens(self)->None:
        self.refresh_token = self.jwt_service.create_access_token(
            user_id=self.user.id,
            expiry=timedelta(days=7),
            refresh_token=True
        )
        self.access_token = self.jwt_service.create_access_token(
            user_id=self.user.id,
            expiry=timedelta(minutes=15),
            refresh_token=False
        )
    def __format_response(self)->Dict:
        response = {
            "success":True,
            "message":"logado com sucesso",
            "refresh_token":self.refresh_token,
            "access_token":self.access_token,
            "user":{
                "email":self.user.email,
                "name":self.user.nome,
                "is_verified":self.user.is_verified
            }
        }
        return response