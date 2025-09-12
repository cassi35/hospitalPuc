from typing import Dict
from src.domain.usecases.funcionario.insert_funcionario import FuncionarioInsertUseCase as FuncionarioInsertInterface
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface 
from src.infra.db.entities.funcionario import Funcionario

class FuncionarioInsertUseCase(FuncionarioInsertInterface):
    def __init__(self, funcionario_repository: FuncionarioRepositoryInterface):
        self.funcionario_repository = funcionario_repository
    
    def insert(self, funcionario: Funcionario) -> Dict:
        pass
