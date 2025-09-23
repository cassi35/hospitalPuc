from src.infra.db.repositories.internacao_repository import InternacaoRepository
from src.infra.db.repositories.leito_repository import LeitoRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.presentation.controllers.internacao.update_internacao_controller import InternacaoUpdateController
from src.data.usecases.internacao.update_internacao import InternacaoUpdateUseCase
def update_internacao_composer():
    internacao_repository = InternacaoRepository()
    leito_repository = LeitoRepository()
    medico_repository = MedicoRepository()
    paciente_repository = PacienteRepository()
    usecase = InternacaoUpdateUseCase(
        internacao_repository=internacao_repository,
        leito_repository=leito_repository,
        medico_repository=medico_repository,
        paciente_repository=paciente_repository
    )
    controller = InternacaoUpdateController(usecase=usecase)
    return controller.handle