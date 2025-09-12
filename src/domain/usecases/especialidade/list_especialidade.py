from abc import ABC, abstractmethod
from typing import List, Dict

class EspecialidadeListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all especialidades usecase"""
        pass
