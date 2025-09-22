from src.presentation.controllers.especialidade.delete_especialidade_controller import EspecialidadeDeleteController
from src.data.usecases.especialidade.delete_especialidade import EspecialidadeDeleteUseCase
from src.infra.db.repositories.especialidade_repository import EspecialidadeRepository
def delete_especialidade_composer():
    repository = EspecialidadeRepository()
    usecase = EspecialidadeDeleteUseCase(
        especialidade_repository=repository
    )
    controller = EspecialidadeDeleteController(usecase=usecase)
    return controller.handle