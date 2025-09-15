from typing import Dict
from src.infra.db.entities.funcionario import Funcionario
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface

class FuncionarioInsertSpy(FuncionarioRepositoryInterface):
    def __init__(self) -> None:
        self.insert_funcionario_attributes = {}
        self.insert_funcionario_call_count = 0

    def insert_funcionario(self, funcionario: Funcionario) -> None:
        self.insert_funcionario_attributes = vars(funcionario)
        self.insert_funcionario_call_count += 1
