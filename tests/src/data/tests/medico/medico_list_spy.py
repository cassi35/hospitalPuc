from typing import List, Dict
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface

class MedicoListSpy(MedicoRepositoryInterface):
    def __init__(self) -> None:
        self.list_medico_call_count = 0
        self.list_medico_return = []

    def list_medico(self) -> List[Dict]:
        self.list_medico_call_count += 1
        return self.list_medico_return
