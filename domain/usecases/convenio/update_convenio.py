from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.convenio import Convenio

class ConvenioUpdateUseCase(ABC):
    @abstractmethod
    def update(self, convenio_id: int, convenio: Convenio) -> Dict:
        """Update existing convenio usecase"""
        pass
