from src.domain.usecases.email.send_welcome import SendWelcomeEmailUsecase as SendWelcomeEmailUsecaseInterface
from src.data.interfaces.stmp_service_interface import SMTPServiceInterface
from src.domain.models.user_email import UserEmail
from src.infra.email.stmp_adapter_service import SMTPEmailService
from src.errors.types.http_bad_request import HttpBadRequestError
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface
from src.data.interfaces.auth_interface import AuthRepositoryInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
class SendWelcomeEmailUsecase(SendWelcomeEmailUsecaseInterface):
    def __init__(self,email_service:SMTPServiceInterface,medico_repository:MedicoRepositoryInterface,funcionario_repository:FuncionarioRepositoryInterface,paciente_repository:PacienteRepositoryInterface,auth_repository:AuthRepositoryInterface):
        self.email_service = email_service
        self.medico_repository = medico_repository
        self.funcionario_repository = funcionario_repository
        self.paciente_repository = paciente_repository
        self.auth_repository = auth_repository
    def send_email(self, email: str,name:str) -> dict:
        self.__validate_email(email=email)
        self.__validate_name(name=name)
        self.__exists_email(email=email)
        self.__execute(email=email,name=name)
        return self.__format_response(email=email)
    def __validate_name(self,name:str)-> None:
        if not name:
            raise HttpBadRequestError("Nome é obrigatório")
        if len(name) < 3:
            raise HttpBadRequestError("Nome deve ter no mínimo 3 caracteres")
        if len(name) > 100:
            raise HttpBadRequestError("Nome deve ter no máximo 100 caracteres")
    def __validate_email(self,email:str)-> None:
        if not email:
            raise HttpBadRequestError("Email é obrigatório")
        if "@" not in email or "." not in email:
            raise HttpBadRequestError("Email inválido")
    def __exists_email(self,email:str)->None:
        medico =self.medico_repository.findByEmail(email=email)
        funcionario =self.funcionario_repository.findByEmail(email=email)
        paciente =self.paciente_repository.findByEmail(email=email)
        auth = self.auth_repository.get_user_by_email(email=email)
        if not medico and not funcionario and not paciente and not auth:
            raise HttpBadRequestError("Email não cadastrado")
    def __execute(self,email:str,name:str)->None: 
            user_email = UserEmail(email=email,name=name)
            send_email = self.email_service.send_welcome_email(email=user_email)
            if not send_email:
                 raise HttpBadRequestError("Erro ao enviar email")

    def __format_response(self,email:str)->dict:
        response = {
            "success":True,
            "message":"Email de boas vindas enviado com sucesso",
            "email":email
        }
        return response
