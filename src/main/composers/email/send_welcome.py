from src.presentation.controllers.email.send_welcome import SendWelcomeEmailController
from src.data.usecases.email.send_welcome import SendWelcomeEmailUsecase
from src.infra.email.stmp_adapter_service import SMTPEmailService
from src.infra.db.repositories.funcionario_repository import FuncionarioRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.infra.db.repositories.paciente_repository import PacienteRepository
def send_welcome_email_composer():
    stmp = SMTPEmailService()
    paciente = PacienteRepository()
    medico = MedicoRepository()
    funcionario = FuncionarioRepository()
    usecase = SendWelcomeEmailUsecase(
        email_service=stmp,
        medico_repository=medico,
        funcionario_repository=funcionario,
        paciente_repository=paciente
    )
    controller = SendWelcomeEmailController(usecase=usecase)
    return controller.handle