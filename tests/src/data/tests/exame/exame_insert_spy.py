from typing import Dict
from src.infra.db.entities.exame import Exame
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface

class ExameInsertSpy(ExameRepositoryInterface):
    def __init__(self) -> None:
        self.insert_exame_attributes = {}
        self.insert_exame_call_count = 0

    def insert_exame(self, exame: Exame) -> None:
        self.insert_exame_attributes = vars(exame)
        self.insert_exame_call_count += 1
