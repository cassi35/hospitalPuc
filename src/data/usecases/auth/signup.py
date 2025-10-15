from src.domain.usecases.auth.signup import SignupUseCase
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
from src.errors.types.ErrorInsertCache import ErrorInsertCache
import re 
class SignupUseCaseImpl(SignupUseCase):
    def __init__(self,auth_repository:AuthRepositoryInterface,jwt_service:JWTServiceInterface,email_service:SMTPServiceInterface,auth_cache:AuthCacheInterface,password_service:PasswordServiceInterface,token_service:URSafeTokenServiceInterface):
        self.auth_repository = auth_repository
        self.jwt_service = jwt_service
        self.email_service = email_service
        self.auth_cache = auth_cache
        self.password_service = password_service
        self.token_service = token_service
        self.token = None
    def signup(self, auth:dict)->dict:
        self.__validate_auth(auth=auth)
        self.__create_token(auth=auth)
        self.__create_user(auth=auth)
        self.__send_verification_email(email=auth['email'])
        return self.__format_response(email=auth['email']) 
    def __validate_auth(self,auth:dict)->None:
        if not auth['email'] or re.match(r"[^@]+@[^@]+\.[^@]+", auth['email']) is None:
            raise HttpBadRequestError("Email inválido")
        if len(auth['senha']) >255 or len(auth['senha']) < 6:
            raise HttpBadRequestError("Senha deve ter entre 6 e 255 caracteres")
        if not auth['nome'] or len(auth['nome']) > 255:
            raise HttpBadRequestError("Nome é obrigatório e deve ter no máximo 255 caracteres")
        if auth['role'] and auth['role'] not in ["Paciente","Medico","Funcionario"]:
            raise HttpBadRequestError("Role inválida")
        if self.auth_repository.get_user_by_email(email=auth['email']):
            raise UserAlreadyExists("Usuário com esse email já existe")
    def __create_token(self,auth:dict)->None:
        token = self.token_service.create_url_safe_token(
            data=auth
        )
        key = f"verify_email:{token}"
        user = self.auth_cache.get_temp_token(key=key)
        if user:
            raise UserAlreadyExists("user already exists in cache")
        self.token = token
    def __create_user(self,auth:dict)->None:
        hash_password = self.password_service.hash_password(
            password=auth['senha']
        )
        auth['senha'] = hash_password
        key = f"verify_email:{self.token}"
        user = self.auth_cache.store_temp_token(
            key=key,
            value=auth
        )
        if user == False:
            raise ErrorInsertCache("Erro ao inserir usuário no cache")
    def __send_verification_email(self,email:str)->None:
        self.email_service.send_token(email=email,token=self.token)
    def __format_response(self,email:str)->dict:
        response = {
            "success":True,
            "message":"Usuário criado com sucesso. Verifique seu email para ativar a conta.",
            "email":email
        }
        return response
        
