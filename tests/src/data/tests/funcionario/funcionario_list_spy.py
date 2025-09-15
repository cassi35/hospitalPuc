from typing import List, Dict
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface

class FuncionarioListSpy(FuncionarioRepositoryInterface):
    def __init__(self) -> None:
        self.list_funcionario_call_count = 0
        self.list_funcionario_return = []

    def list_funcionario(self) -> List[Dict]:
        self.list_funcionario_call_count += 1
        return self.list_funcionario_return
