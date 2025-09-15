from typing import List, Dict
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface

class FinanceiroListSpy(FinanceiroRepositoryInterface):
    def __init__(self) -> None:
        self.list_financeiro_call_count = 0
        self.list_financeiro_return = []

    def list_financeiro(self) -> List[Dict]:
        self.list_financeiro_call_count += 1
        return self.list_financeiro_return
