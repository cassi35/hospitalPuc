from src.domain.usecases.email.send_reset_password import ResetPasswordEmailUsecase as ResetPasswordEmailUsecaseInterface
from src.infra.email.stmp_adapter_service import SMTPEmailService
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from data.interfaces.stmp_service_interface import SMTPServiceInterface
from src.domain.usecases.email.send_reset_password import ResetPasswordEmailUsecase
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
class ResetPasswordEmailUsecase(ResetPasswordEmailUsecaseInterface):
    def __init__(self,email_service:SMTPServiceInterface,medico_repository:MedicoRepositoryInterface,funcionario_repository:FuncionarioRepositoryInterface,paciente_repository:PacienteRepositoryInterface):
        self.email_service = email_service
        self.medico_repository = medico_repository
        self.funcionario_repository = funcionario_repository
        self.paciente_repository = paciente_repository
    def send_email(self, email: str,token:int) -> dict:
        self.__validate_email(email=email)
        self.__validate_token(token=token)
        self.__exists_email(email=email)
        self.__execute(email=email,token=token)
        return self.__format_response(email=email)
    def __validate_token(self,token:int)-> None:
        if not token:
            raise HttpBadRequestError("Token é obrigatório")
        if len(str(token)) != 4:
            raise HttpBadRequestError("Token inválido")
    def __validate_email(self,email:str)-> None:
        if not email:
            raise HttpNotFoundError("Email é obrigatório")
        if "@" not in email or "." not in email:
            raise HttpBadRequestError("Email inválido")
    def __exists_email(self,email:str)->None:
        medico =self.medico_repository.findByEmail(email=email)
        funcionario =self.funcionario_repository.findByEmail(email=email)
        paciente =self.paciente_repository.findByEmail(email=email)
        if not medico and not funcionario and not paciente:
            raise HttpNotFoundError("Email não cadastrado")
    def __execute(self,email:str,token:int) ->None:
        send_email = self.email_service.send_reset_password_email(email=email,token=token)
        if not send_email:
            raise HttpBadRequestError("Erro ao enviar email")
    def __format_response(self,email:str)->dict:
        response = {
            "success":True,
            "message":"Email para resetar senha enviado com sucesso",
            "email":email
        }
        return response