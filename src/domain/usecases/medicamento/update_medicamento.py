from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.medicamento import Medicamento

class MedicamentoUpdateUseCase(ABC):
    @abstractmethod
    def update(self, medicamento_id: int, medicamento: Medicamento) -> Dict:
        """Update existing medicamento usecase"""
        pass
