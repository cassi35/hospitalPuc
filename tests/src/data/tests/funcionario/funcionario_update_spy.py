from typing import Dict
from src.infra.db.entities.funcionario import Funcionario
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface

class FuncionarioUpdateSpy(FuncionarioRepositoryInterface):
    def __init__(self) -> None:
        self.update_funcionario_attributes = {}
        self.update_funcionario_call_count = 0

    def update_funcionario(self, funcionario_id: int, funcionario: Funcionario) -> None:
        self.update_funcionario_attributes = vars(funcionario)
        self.update_funcionario_attributes['id'] = funcionario_id
        self.update_funcionario_call_count += 1
