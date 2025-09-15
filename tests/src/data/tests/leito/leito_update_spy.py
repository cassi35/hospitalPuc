from typing import Dict
from src.infra.db.entities.leito import Leito
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface

class LeitoUpdateSpy(LeitoRepositoryInterface):
    def __init__(self) -> None:
        self.update_leito_attributes = {}
        self.update_leito_call_count = 0

    def update_leito(self, leito_id: int, leito: Leito) -> None:
        self.update_leito_attributes = vars(leito)
        self.update_leito_attributes['id'] = leito_id
        self.update_leito_call_count += 1
