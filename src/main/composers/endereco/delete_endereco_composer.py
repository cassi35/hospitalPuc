from src.presentation.controllers.endereco.delete_endereco_controller import EnderecoDeleteController
from src.data.usecases.endereco.delete_endereco import EnderecoDeleteUseCase
from src.infra.db.repositories.endereco_reposotory import EnderecoRepository
def delete_endereco_composer():
    repository = EnderecoRepository()
    usecase = EnderecoDeleteUseCase(
        endereco_repository=repository
    )
    controller = EnderecoDeleteController(usecase=usecase)
    return controller.handle