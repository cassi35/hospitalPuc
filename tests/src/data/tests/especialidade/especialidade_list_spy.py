from typing import List, Dict
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface

class EspecialidadeListSpy(EspecialidadeRepositoryInterface):
    def __init__(self) -> None:
        self.list_especialidade_call_count = 0
        self.list_especialidade_return = []

    def list_especialidade(self) -> List[Dict]:
        self.list_especialidade_call_count += 1
        return self.list_especialidade_return
