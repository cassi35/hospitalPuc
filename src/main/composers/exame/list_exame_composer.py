from src.presentation.controllers.exame.list_exame_controller import ExameListController
from src.data.usecases.exame.list_exame import ExameListUseCase
from src.infra.db.repositories.exame_repository import ExameRepository
def list_exame_composer():
    repository = ExameRepository()
    usecase = ExameListUseCase(
        exame_repository=repository
    )
    controller = ExameListController(usecase=usecase)
    return controller.handle