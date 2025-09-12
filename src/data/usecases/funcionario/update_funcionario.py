from typing import Dict
from src.domain.usecases.funcionario.update_funcionario import FuncionarioUpdateUseCase as FuncionarioUpdateInterface
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface 
from src.infra.db.entities.funcionario import Funcionario

class FuncionarioUpdateUseCase(FuncionarioUpdateInterface):
    def __init__(self, funcionario_repository: FuncionarioRepositoryInterface):
        self.funcionario_repository = funcionario_repository
    
    def update(self, funcionario_id: int, funcionario: Funcionario) -> Dict:
        pass
