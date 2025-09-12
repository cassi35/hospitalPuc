from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.endereco import Endereco

class EnderecoInsertUseCase(ABC):
    @abstractmethod
    def insert(self, endereco: Endereco) -> Dict:
        """Insert new endereco usecase"""
        pass
