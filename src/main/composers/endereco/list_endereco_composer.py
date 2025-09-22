from src.presentation.controllers.endereco.list_endereco_controller import EnderecoListController
from src.data.usecases.endereco.list_endereco import EnderecoListUseCase
from src.infra.db.repositories.endereco_reposotory import EnderecoRepository
def list_endereco_composer():
    repository = EnderecoRepository()
    usecase = EnderecoListUseCase(
        endereco_repository=repository
    )
    controller = EnderecoListController(usecase=usecase)
    return controller.handle