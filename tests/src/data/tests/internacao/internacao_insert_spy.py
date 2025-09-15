from typing import Dict
from src.infra.db.entities.internacao import Internacao
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface

class InternacaoInsertSpy(InternacaoRepositoryInterface):
    def __init__(self) -> None:
        self.insert_internacao_attributes = {}
        self.insert_internacao_call_count = 0

    def insert_internacao(self, internacao: Internacao) -> None:
        self.insert_internacao_attributes = vars(internacao)
        self.insert_internacao_call_count += 1
