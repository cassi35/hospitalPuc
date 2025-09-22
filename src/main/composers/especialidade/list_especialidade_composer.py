from src.presentation.controllers.especialidade.list_especialidade_controller import EspecialidadeListController
from src.data.usecases.especialidade.list_especialidade import EspecialidadeListUseCase
from src.infra.db.repositories.especialidade_repository import EspecialidadeRepository
def list_especialidade_composer():
    repository = EspecialidadeRepository()
    usecase = EspecialidadeListUseCase(
        especialidade_repository=repository
    )
    controller = EspecialidadeListController(usecase=usecase)
    return controller.handle