from typing import Dict
from src.infra.db.entities.prescricao import Prescricao
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface

class PrescricaoInsertSpy(PrescricaoRepositoryInterface):
    def __init__(self) -> None:
        self.insert_prescricao_attributes = {}
        self.insert_prescricao_call_count = 0

    def insert_prescricao(self, prescricao: Prescricao) -> None:
        self.insert_prescricao_attributes = vars(prescricao)
        self.insert_prescricao_call_count += 1
