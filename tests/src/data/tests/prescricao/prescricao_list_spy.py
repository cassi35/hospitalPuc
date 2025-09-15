from typing import List, Dict
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface

class PrescricaoListSpy(PrescricaoRepositoryInterface):
    def __init__(self) -> None:
        self.list_prescricao_call_count = 0
        self.list_prescricao_return = []

    def list_prescricao(self) -> List[Dict]:
        self.list_prescricao_call_count += 1
        return self.list_prescricao_return
