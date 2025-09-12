from typing import Dict
from src.domain.usecases.financeiro.insert_financeiro import FinanceiroInsertUseCase as FinanceiroInsertInterface
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface 
from src.infra.db.entities.financeiro import Financeiro

class FinanceiroInsertUseCase(FinanceiroInsertInterface):
    def __init__(self, financeiro_repository: FinanceiroRepositoryInterface):
        self.financeiro_repository = financeiro_repository
    
    def insert(self, financeiro: Financeiro) -> Dict:
        pass
