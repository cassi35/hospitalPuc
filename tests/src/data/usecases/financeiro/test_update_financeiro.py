from typing import Dict
from src.domain.usecases.financeiro.update_financeiro import FinanceiroUpdateUseCase as FinanceiroUpdateInterface
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface 
from src.infra.db.entities.financeiro import Financeiro

class FinanceiroUpdateUseCase(FinanceiroUpdateInterface):
    def __init__(self, financeiro_repository: FinanceiroRepositoryInterface):
        self.financeiro_repository = financeiro_repository
    
    def update(self, financeiro_id: int, financeiro: Financeiro) -> Dict:
        pass
