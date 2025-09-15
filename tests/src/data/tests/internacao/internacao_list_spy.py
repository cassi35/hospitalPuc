from typing import List, Dict
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface

class InternacaoListSpy(InternacaoRepositoryInterface):
    def __init__(self) -> None:
        self.list_internacao_call_count = 0
        self.list_internacao_return = []

    def list_internacao(self) -> List[Dict]:
        self.list_internacao_call_count += 1
        return self.list_internacao_return
