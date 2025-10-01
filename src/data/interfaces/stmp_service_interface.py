from abc import ABC, abstractmethod
from src.domain.models.user_email import UserEmail
class SMTPServiceInterface(ABC):
    @abstractmethod
    def send_token(self, token:str, email:str) -> bool:
        pass
    @abstractmethod
    def send_welcome_email(self, user:UserEmail)-> bool:
        pass
    @abstractmethod
    def send_reset_password_email(self, token:str, email:str) -> bool:
        pass
    @abstractmethod
    def resend_verification_token(self, token:str, email:str) -> bool:
        pass