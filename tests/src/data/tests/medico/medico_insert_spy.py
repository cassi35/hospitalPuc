from typing import Dict
from src.infra.db.entities.medico import Medico
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface

class MedicoInsertSpy(MedicoRepositoryInterface):
    def __init__(self) -> None:
        self.insert_medico_attributes = {}
        self.insert_medico_call_count = 0

    def insert_medico(self, medico: Medico) -> None:
        self.insert_medico_attributes = vars(medico)
        self.insert_medico_call_count += 1
