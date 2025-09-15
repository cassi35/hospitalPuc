from typing import List, Dict
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface

class ExameListSpy(ExameRepositoryInterface):
    def __init__(self) -> None:
        self.list_exame_call_count = 0
        self.list_exame_return = []

    def list_exame(self) -> List[Dict]:
        self.list_exame_call_count += 1
        return self.list_exame_return
