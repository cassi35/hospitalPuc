from src.presentation.controllers.endereco.update_endereco_controller import EnderecoUpdateController
from src.infra.db.repositories.endereco_reposotory import EnderecoRepository
from src.data.usecases.endereco.update_endereco import EnderecoUpdateUseCase
def update_endereco_composer():
    repository = EnderecoRepository()
    usecase = EnderecoUpdateUseCase(
        endereco_repository=repository
    )
    controller = EnderecoUpdateController(usecase=usecase)
    return controller.handle