from src.presentation.controllers.internacao.insert_internacao_controller import InternacaoInsertController
from src.data.usecases.internacao.insert_internacao import InternacaoInsertUseCase
from src.infra.db.repositories.internacao_repository import InternacaoRepository
from src.infra.db.repositories.leito_repository import LeitoRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.infra.db.repositories.paciente_repository import PacienteRepository
def insert_internacao_composer():
    internacao_repository = InternacaoRepository()
    leito_repository = LeitoRepository()
    medico_repository = MedicoRepository()
    paciente_repository = PacienteRepository()
    usecase = InternacaoInsertUseCase(
        internacao_repository=internacao_repository,
        leito_repository=leito_repository,
        medico_repository=medico_repository,
        paciente_repository=paciente_repository
    )
    controller = InternacaoInsertController(usecase=usecase)
    return controller.handle