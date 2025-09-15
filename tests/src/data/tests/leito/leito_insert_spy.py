from typing import Dict
from src.infra.db.entities.leito import Leito
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface

class LeitoInsertSpy(LeitoRepositoryInterface):
    def __init__(self) -> None:
        self.insert_leito_attributes = {}
        self.insert_leito_call_count = 0

    def insert_leito(self, leito: Leito) -> None:
        self.insert_leito_attributes = vars(leito)
        self.insert_leito_call_count += 1
