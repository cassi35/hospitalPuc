from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.financeiro import Financeiro

class FinanceiroInsertUseCase(ABC):
    @abstractmethod
    def insert(self, financeiro: Financeiro) -> Dict:
        """Insert new financeiro usecase"""
        pass
