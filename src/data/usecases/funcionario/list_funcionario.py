from typing import List, Dict
from src.domain.usecases.funcionario.list_funcionario import FuncionarioListUseCase as FuncionarioListInterface
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface

class FuncionarioListUseCase(FuncionarioListInterface):
    def __init__(self, funcionario_repository: FuncionarioRepositoryInterface):
        self.funcionario_repository = funcionario_repository
    
    def list(self) -> List[Dict]:
        pass
