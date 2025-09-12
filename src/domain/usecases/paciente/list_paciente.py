from abc import ABC, abstractmethod
from typing import List, Dict

class PacienteListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all pacientes usecase"""
        pass
