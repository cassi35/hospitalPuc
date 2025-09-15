from typing import Dict
from src.infra.db.entities.financeiro import Financeiro
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface

class FinanceiroUpdateSpy(FinanceiroRepositoryInterface):
    def __init__(self) -> None:
        self.update_financeiro_attributes = {}
        self.update_financeiro_call_count = 0

    def update_financeiro(self, financeiro_id: int, financeiro: Financeiro) -> None:
        self.update_financeiro_attributes = vars(financeiro)
        self.update_financeiro_attributes['id'] = financeiro_id
        self.update_financeiro_call_count += 1
