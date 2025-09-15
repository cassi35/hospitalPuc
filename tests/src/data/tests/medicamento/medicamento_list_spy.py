from typing import List, Dict
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface

class MedicamentoListSpy(MedicamentoRepositoryInterface):
    def __init__(self) -> None:
        self.list_medicamento_call_count = 0
        self.list_medicamento_return = []

    def list_medicamento(self) -> List[Dict]:
        self.list_medicamento_call_count += 1
        return self.list_medicamento_return
