from typing import List, Dict
from src.domain.usecases.financeiro.list_financeiro import FinanceiroListUseCase as FinanceiroListInterface
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface

class FinanceiroListUseCase(FinanceiroListInterface):
    def __init__(self, financeiro_repository: FinanceiroRepositoryInterface):
        self.financeiro_repository = financeiro_repository
    
    def list(self) -> List[Dict]:
        pass
