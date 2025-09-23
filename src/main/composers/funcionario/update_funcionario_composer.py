from src.presentation.controllers.funcionario.update_funcionario_controller import FuncionarioUpdateController
from src.data.usecases.funcionario.update_funcionario import FuncionarioUpdateUseCase
from src.infra.db.repositories.funcionario_repository import FuncionarioRepository
from src.infra.db.repositories.setor_repository import SetorRepository
def update_funcionario_composer():
    funcionario_repository = FuncionarioRepository()
    setor_repository = SetorRepository()
    usecase = FuncionarioUpdateUseCase(
        funcionario_repository=funcionario_repository,
        setor_repository=setor_repository
    )
    controller = FuncionarioUpdateController(usecase=usecase)
    return controller.handle