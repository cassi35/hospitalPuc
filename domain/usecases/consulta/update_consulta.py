from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.consulta import Consulta

class ConsultaUpdateUseCase(ABC):
    @abstractmethod
    def update(self, consulta_id: int, consulta: Consulta) -> Dict:
        """Update existing consulta usecase"""
        pass
