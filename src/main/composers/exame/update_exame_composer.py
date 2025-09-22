from src.infra.db.repositories.exame_repository import ExameRepository
from src.infra.db.repositories.paciente_repository  import PacienteRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.presentation.controllers.exame.update_exame_controller import ExameUpdateController
from src.data.usecases.exame.update_exame import ExameUpdateUseCase
def update_exame_composer():
    exame_repository = ExameRepository()
    paciente_repository = PacienteRepository()
    medico_repository = MedicoRepository()
    usecase = ExameUpdateUseCase(
        exame_repository=exame_repository,
        paciente_repository=paciente_repository,
        medico_repository=medico_repository
    )
    controller = ExameUpdateController(usecase=usecase)
    return controller.handle