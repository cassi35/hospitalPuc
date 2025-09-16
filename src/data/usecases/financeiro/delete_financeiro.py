from src.domain.usecases.financeiro.delete_financeiro import FinanceiroDeleteUseCase as FinanceiroDeleteInterface
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface
from typing import Dict

class FinanceiroDeleteUseCase(FinanceiroDeleteInterface):
    def __init__(self, financeiro_repository: FinanceiroRepositoryInterface):
        self.financeiro_repository = financeiro_repository
    
    def delete(self, financeiro_id: int) -> Dict:
        pass
