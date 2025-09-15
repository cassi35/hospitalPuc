from typing import List, Dict
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface

class LeitoListSpy(LeitoRepositoryInterface):
    def __init__(self) -> None:
        self.list_leito_call_count = 0
        self.list_leito_return = []

    def list_leito(self) -> List[Dict]:
        self.list_leito_call_count += 1
        return self.list_leito_return
