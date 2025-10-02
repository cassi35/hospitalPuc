from src.presentation.controllers.email.send_reset_password import ResetPasswordEmailController
from src.data.usecases.email.send_reset_password import ResetPasswordEmailUsecase
from src.infra.email.stmp_adapter_service import SMTPEmailService
from src.infra.db.repositories.funcionario_repository import FuncionarioRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.infra.db.repositories.paciente_repository import PacienteRepository
def send_reset_password_composer():
    stmp = SMTPEmailService()
    usecase = ResetPasswordEmailUsecase(
        email_service=stmp,
        medico_repository=MedicoRepository(),
        funcionario_repository=FuncionarioRepository(),
        paciente_repository=PacienteRepository()
    )
    controller = ResetPasswordEmailController(usecase=usecase)
    return controller.handle