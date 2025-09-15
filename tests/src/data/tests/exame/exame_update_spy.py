from typing import Dict
from src.infra.db.entities.exame import Exame
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface

class ExameUpdateSpy(ExameRepositoryInterface):
    def __init__(self) -> None:
        self.update_exame_attributes = {}
        self.update_exame_call_count = 0

    def update_exame(self, exame_id: int, exame: Exame) -> None:
        self.update_exame_attributes = vars(exame)
        self.update_exame_attributes['id'] = exame_id
        self.update_exame_call_count += 1
