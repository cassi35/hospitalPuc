from typing import Dict
from src.infra.db.entities.prescricao import Prescricao
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface

class PrescricaoUpdateSpy(PrescricaoRepositoryInterface):
    def __init__(self) -> None:
        self.update_prescricao_attributes = {}
        self.update_prescricao_call_count = 0

    def update_prescricao(self, prescricao_id: int, prescricao: Prescricao) -> None:
        self.update_prescricao_attributes = vars(prescricao)
        self.update_prescricao_attributes['id'] = prescricao_id
        self.update_prescricao_call_count += 1
