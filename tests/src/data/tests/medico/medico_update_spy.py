from typing import Dict
from src.infra.db.entities.medico import Medico
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface

class MedicoUpdateSpy(MedicoRepositoryInterface):
    def __init__(self) -> None:
        self.update_medico_attributes = {}
        self.update_medico_call_count = 0

    def update_medico(self, medico_id: int, medico: Medico) -> None:
        self.update_medico_attributes = vars(medico)
        self.update_medico_attributes['id'] = medico_id
        self.update_medico_call_count += 1
