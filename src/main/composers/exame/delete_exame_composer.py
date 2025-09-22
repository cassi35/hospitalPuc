from src.presentation.controllers.exame.delete_exame_controller import ExameDeleteController
from src.data.usecases.exame.delete_exame import ExameDeleteUseCase
from src.infra.db.repositories.exame_repository import ExameRepository
def delete_exame_composer():
    repository = ExameRepository()
    usecase = ExameDeleteUseCase(
        exame_repository=repository
    )
    controller = ExameDeleteController(usecase=usecase)
    return controller.handle