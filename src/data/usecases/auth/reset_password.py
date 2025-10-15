from src.domain.usecases.auth.reset_password import ResetPasswordUseCase as ResetPasswordUseCaseInterface
from src.data.interfaces.auth_cahce_interface import AuthCacheInterface
from src.data.interfaces.password_service_interface import PasswordServiceInterface
from src.data.interfaces.auth_interface import AuthRepositoryInterface
from src.errors.types.ExpiredToken import ExpiredToken 
from src.errors.types.InvalidToken import InvalidToken
from src.errors.types.http_bad_request import HttpBadRequestError
import re
from typing import Dict
class ResetPasswordUseCase(ResetPasswordUseCaseInterface):
    def __init__(self,auth_cache_service:AuthCacheInterface,
                 password_service:PasswordServiceInterface,
                 auth_repository:AuthRepositoryInterface):
        self.auth_cache_service = auth_cache_service
        self.password_service = password_service
        self.auth_repository = auth_repository
        self.key = None 
    def reset_password(self, email:str, token:str, nova_senha:str)-> Dict:
        self.__validate_informations(email=email, token=token, nova_senha=nova_senha)
        self.__verify_token(email=email, token=token)
        self.__update_password(email=email, nova_senha=nova_senha)
        response = self.__format_response(email=email)
        return response 
    def __validate_informations(self,email:str, token:str, nova_senha:str)-> None:
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise HttpBadRequestError("Email inválido.")
        if not token or len(token) < 10:
            raise HttpBadRequestError("Token inválido.")
        if not nova_senha or len(nova_senha) < 6:
            raise HttpBadRequestError("A nova senha deve ter pelo menos 6 caracteres.")
        
    def __verify_token(self,email:str, token:str)-> None:
        key = f"reset_password:{token}"
        get_token = self.auth_cache_service.get_temp_token(key=key)
        if not get_token:
            raise ExpiredToken("Token expirado ou inválido.")
        email_token = get_token["email"]
        if email != email_token:
            raise InvalidToken("Token inválido para o email fornecido.")
        self.key = key
    def __update_password(self,email:str, nova_senha:str)-> None:
        hash_password = self.password_service.hash_password(password=nova_senha)
        user = self.auth_repository.get_user_by_email(email=email)
        if not user:
            raise HttpBadRequestError("Usuário não encontrado.")
        new_user = {
            "email": user.email,
            "nome":user.nome,
            "senha": hash_password,
            "role":user.role,
            "is_verified":user.is_verified
        }
        self.auth_repository.update_user(update_data=new_user,user_id=user.id)
        self.auth_cache_service.delete_temp_token(key=self.key)
    def __format_response(self,email:str)->Dict:
        response = {
            "success": True,
            "message": "Senha redefinida com sucesso.",
            "email": email
        }
        return response