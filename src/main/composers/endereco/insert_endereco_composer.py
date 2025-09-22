from src.presentation.controllers.endereco.insert_endereco_controller import EnderecoInsertController
from src.data.usecases.endereco.insert_endereco import EnderecoInsertUseCase
from src.infra.db.repositories.endereco_reposotory import EnderecoRepository
def insert_endereco_composer():
    repository = EnderecoRepository()
    usecase = EnderecoInsertUseCase(
        endereco_repository=repository
    )
    controller = EnderecoInsertController(usecase=usecase)
    return controller.handle