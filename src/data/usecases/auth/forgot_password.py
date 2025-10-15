from src.data.interfaces.auth_cahce_interface import AuthCacheInterface
from src.data.interfaces.stmp_service_interface import SMTPServiceInterface
from src.data.interfaces.urSafeTokenService_interface import URSafeTokenServiceInterface
from src.domain.usecases.auth.forgot_password import ForgotPasswordUseCase as ForgotPasswordUseCaseInterface
from src.errors.types.ErrorCache import ErrorCache
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.UserAlreadyExists import UserAlreadyExists
from src.data.interfaces.auth_interface import AuthRepositoryInterface
import re 
from typing import Dict
class ForgotPasswordUsecase(ForgotPasswordUseCaseInterface):
    def __init__(self, smtp_service: SMTPServiceInterface, token_service: URSafeTokenServiceInterface, auth_cache: AuthCacheInterface,auth_repository: AuthRepositoryInterface):
        self.smtp_service = smtp_service
        self.token_service = token_service
        self.auth_cache = auth_cache
        self.auth_repository = auth_repository
        self.token = None
    def forgot_password(self, email:str)->Dict:
        self.__validate_informations(email=email)
        self.__create_token(email=email)
        self.__store_token(email=email)
        self.__send_email(email=email)
        response = self.__format_response(email=email)
        return response
    def __validate_informations(self,email:str)-> None:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise HttpBadRequestError("Invalid email format")
        user = self.auth_repository.get_user_by_email(email=email)
        if not user:
            raise HttpNotFoundError("User not found")
    def __create_token(self,email:str)-> None:
        value = {"email":email}
        token = self.token_service.create_url_safe_token(
            data=value
        )
        key = f"forgot_password:{token}"
        user = self.auth_cache.get_temp_token(key=key)
        if user:
            raise UserAlreadyExists("A reset token has already been sent. Please check your email.")
        self.token = token
    def __store_token(self,email:str)-> None:
        key = f"forgot_password:{self.token}"
        value = {"email":email}
        self.auth_cache.store_temp_token(key=key,value=value)
    def __send_email(self,email:str)-> None:
        self.smtp_service.send_reset_password_email(email=email,token=self.token)
    def __format_response(self,email:str)-> Dict:
        response = {
            "success": True,
            "message":f"Password reset email sent to {email}"
        }
        return response