from typing import Dict
from src.infra.db.entities.setor import Setor
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface

class SetorInsertSpy(SetorRepositoryInterface):
    def __init__(self) -> None:
        self.insert_setor_attributes = {}
        self.insert_setor_call_count = 0

    def insert_setor(self, setor: Setor) -> None:
        self.insert_setor_attributes = vars(setor)
        self.insert_setor_call_count += 1
