from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface

class FinanceiroDeleteSpy(FinanceiroRepositoryInterface):
    def __init__(self) -> None:
        self.delete_financeiro_id = None
        self.delete_financeiro_call_count = 0

    def delete_financeiro(self, financeiro_id: int) -> None:
        self.delete_financeiro_id = financeiro_id
        self.delete_financeiro_call_count += 1
