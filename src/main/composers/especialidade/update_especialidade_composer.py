from src.presentation.controllers.especialidade.update_especialidade_controller import EspecialidadeUpdateController
from src.data.usecases.especialidade.update_especialidade import EspecialidadeUpdateUseCase
from src.infra.db.repositories.especialidade_repository import EspecialidadeRepository
def update_especialidade_composer():
    repository = EspecialidadeRepository()
    usecase = EspecialidadeUpdateUseCase(
        especialidade_repository=repository
    )
    controller = EspecialidadeUpdateController(usecase=usecase)
    return controller.handle