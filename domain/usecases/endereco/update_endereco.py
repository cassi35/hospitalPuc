from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.endereco import Endereco

class EnderecoUpdateUseCase(ABC):
    @abstractmethod
    def update(self, endereco_id: int, endereco: Endereco) -> Dict:
        """Update existing endereco usecase"""
        pass
