from typing import List, Dict
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface

class SetorListSpy(SetorRepositoryInterface):
    def __init__(self) -> None:
        self.list_setor_call_count = 0
        self.list_setor_return = []

    def list_setor(self) -> List[Dict]:
        self.list_setor_call_count += 1
        return self.list_setor_return
