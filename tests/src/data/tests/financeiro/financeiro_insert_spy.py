from typing import Dict
from src.infra.db.entities.financeiro import Financeiro
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface

class FinanceiroInsertSpy(FinanceiroRepositoryInterface):
    def __init__(self) -> None:
        self.insert_financeiro_attributes = {}
        self.insert_financeiro_call_count = 0

    def insert_financeiro(self, financeiro: Financeiro) -> None:
        self.insert_financeiro_attributes = vars(financeiro)
        self.insert_financeiro_call_count += 1
