from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.medicamento import Medicamento

class MedicamentoInsertUseCase(ABC):
    @abstractmethod
    def insert(self, medicamento: Medicamento) -> Dict:
        """Insert new medicamento usecase"""
        pass
