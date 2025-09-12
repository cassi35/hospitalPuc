from src.domain.usecases.funcionario.delete_funcionario import FuncionarioDeleteUseCase as FuncionarioDeleteInterface
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface

class FuncionarioDeleteUseCase(FuncionarioDeleteInterface):
    def __init__(self, funcionario_repository: FuncionarioRepositoryInterface):
        self.funcionario_repository = funcionario_repository
    
    def delete(self, funcionario_id: int) -> None:
        pass
