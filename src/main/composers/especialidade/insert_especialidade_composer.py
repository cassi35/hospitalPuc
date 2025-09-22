from src.presentation.controllers.especialidade.insert_especialidade_controller import EspecialidadeInsertController
from src.data.usecases.especialidade.insert_especialidade import EspecialidadeInsertUseCase
from src.infra.db.repositories.especialidade_repository import EspecialidadeRepository
def insert_especialidade_composer():
    repository = EspecialidadeRepository()
    usecase = EspecialidadeInsertUseCase(
        especialidade_repository=repository
    )
    controller = EspecialidadeInsertController(usecase=usecase)
    return controller.handle