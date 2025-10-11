from src.data.interfaces.stmp_service_interface import SMTPServiceInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.data.interfaces.stmp_service_interface import SMTPServiceInterface
from src.domain.usecases.email.send_token import SendVerificationTokenUsecase as SendVerificationTokenUsecaseInterface
class SendVerificationTokenUsecase(SendVerificationTokenUsecaseInterface):
    def __init__(self,email_service:SMTPServiceInterface):
        self.email_service = email_service
    def send_email(self, token:int, email:str)-> dict:
        self.__validate_email(email=email)
        self.__validate_token(token=token)
        self.__execute(token=token,email=email)
        return self.__format_response(email=email) 
    def __validate_email(self,email:str)-> None:
        if not email:
            raise HttpBadRequestError("Email é obrigatório")
        if "@" not in email or "." not in email:
            raise HttpBadRequestError("Email inválido")
    def __validate_token(self,token:int)-> None:
        if not token:
            raise HttpBadRequestError("Token é obrigatório")
    def __execute(self,token:int,email:str)->None:
        send_email = self.email_service.send_token(email=email,token=token)
        if not send_email:
            raise HttpBadRequestError("Erro ao enviar email")
    def __format_response(self,email:str)->dict:
        response = {
            "success":True,
            "message":"Email enviado com sucesso",
            "email":email
        }
        return response