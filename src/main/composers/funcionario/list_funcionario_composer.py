from src.presentation.controllers.funcionario.list_funcionario_controller import FuncionarioListController
from src.data.usecases.funcionario.list_funcionario import FuncionarioListUseCase
from src.infra.db.repositories.funcionario_repository import FuncionarioRepository
def list_funcionario_composer():
    repository = FuncionarioRepository()
    usecase = FuncionarioListUseCase(
        funcionario_repository=repository
    )
    controller = FuncionarioListController(usecase=usecase)
    return controller.handle