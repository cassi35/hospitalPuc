from typing import Dict
from src.infra.db.entities.setor import Setor
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface

class SetorUpdateSpy(SetorRepositoryInterface):
    def __init__(self) -> None:
        self.update_setor_attributes = {}
        self.update_setor_call_count = 0

    def update_setor(self, setor_id: int, setor: Setor) -> None:
        self.update_setor_attributes = vars(setor)
        self.update_setor_attributes['id'] = setor_id
        self.update_setor_call_count += 1
