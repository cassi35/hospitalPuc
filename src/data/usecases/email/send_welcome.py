from src.domain.usecases.email.send_welcome import SendWelcomeEmailUsecase as SendWelcomeEmailUsecaseInterface
from src.data.interfaces.stmp_service_interface import SMTPServiceInterface
from src.domain.models.user_email import UserEmail
from src.errors.types.http_bad_request import HttpBadRequestError
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
class SendWelcomeEmailUsecase(SendWelcomeEmailUsecaseInterface):
    def __init__(self,email_service:SMTPServiceInterface,medico_repository:MedicoRepositoryInterface,funcionario_repository:FuncionarioRepositoryInterface,paciente_repository:PacienteRepositoryInterface):
        self.email_service = email_service
        self.medico_repository = medico_repository
        self.funcionario_repository = funcionario_repository
        self.paciente_repository = paciente_repository
    def send_email(self, email: str) -> dict:pass
    def __validate_email(self,email:str)-> None:pass
    def __execute(self,email:str)->None:pass
    def __format_response(self,email:str)->dict:pass

