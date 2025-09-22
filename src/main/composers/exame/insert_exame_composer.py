from src.presentation.controllers.exame.insert_exame_controller import ExameInsertController
from src.data.usecases.exame.insert_exame import ExameInsertUseCase
from src.infra.db.repositories.exame_repository import ExameRepository
from src.infra.db.repositories.paciente_repository  import PacienteRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
def insert_exame_composer():
    exame_repository = ExameRepository()
    paciente_repository = PacienteRepository()
    medico_repository = MedicoRepository()
    usecase = ExameInsertUseCase(
        exame_repository=exame_repository,
        paciente_repository=paciente_repository,
        medico_repository=medico_repository
    )
    controller = ExameInsertController(usecase=usecase)
    return controller.handle