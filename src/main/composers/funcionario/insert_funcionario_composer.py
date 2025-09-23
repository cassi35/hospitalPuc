from src.presentation.controllers.funcionario.insert_funcionario_controller import FuncionarioInsertController
from src.data.usecases.funcionario.insert_funcionario import FuncionarioInsertUseCase
from src.infra.db.repositories.funcionario_repository import FuncionarioRepository
from src.infra.db.repositories.setor_repository import SetorRepository
def insert_funcionario_composer():
    funcionario_repository = FuncionarioRepository()
    setor_repository = SetorRepository()
    usecase = FuncionarioInsertUseCase(
        funcionario_repository=funcionario_repository,
        setor_repository=setor_repository
    )
    controller = FuncionarioInsertController(usecase=usecase)
    return controller.handle