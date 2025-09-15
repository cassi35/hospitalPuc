from typing import Dict
from src.infra.db.entities.internacao import Internacao
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface

class InternacaoUpdateSpy(InternacaoRepositoryInterface):
    def __init__(self) -> None:
        self.update_internacao_attributes = {}
        self.update_internacao_call_count = 0

    def update_internacao(self, internacao_id: int, internacao: Internacao) -> None:
        self.update_internacao_attributes = vars(internacao)
        self.update_internacao_attributes['id'] = internacao_id
        self.update_internacao_call_count += 1
