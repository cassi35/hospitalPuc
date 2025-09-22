from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.convenio_model import Convenio

class ConvenioUpdateUseCase(ABC):
    @abstractmethod
    def update(self, convenio_id: int, convenio: Convenio) -> Dict:
        """Update existing convenio usecase"""
        pass
