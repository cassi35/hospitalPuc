from src.data.interfaces.stmp_service_interface import SMTPServiceInterface
from src.domain.models.user_email import UserEmail as UserEmailDomain
class StmpEmailServiceSpy(SMTPServiceInterface):
    def __init__(self):
        self.send_emails = []
    def send_reset_password_email(self, token:int, email:str)-> bool:
        return True
    def send_token(self, token:int, email:str)-> bool:
        return True
    def send_welcome_email(self, user:UserEmailDomain)-> bool:
        return True
    def resend_verification_token(self, token:int, email:str)-> bool:
        return True