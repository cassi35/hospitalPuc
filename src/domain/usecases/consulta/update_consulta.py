from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.consulta_model import Consulta

class ConsultaUpdateUseCase(ABC):
    @abstractmethod
    def update(self, consulta_id: int, consulta: Consulta) -> Dict:
        """Update existing consulta usecase"""
        pass
