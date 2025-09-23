from src.presentation.controllers.funcionario.delete_funcionario_controller import FuncionarioDeleteController
from src.data.usecases.funcionario.delete_funcionario import FuncionarioDeleteUseCase
from src.infra.db.repositories.funcionario_repository import FuncionarioRepository
def delete_funcionario_composer():
    repository = FuncionarioRepository()
    usecase = FuncionarioDeleteUseCase(
        funcionario_repository=repository
    )
    controller = FuncionarioDeleteController(usecase=usecase)
    return controller.handle