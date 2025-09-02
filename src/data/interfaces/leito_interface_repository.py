from abc import ABC, abstractmethod
from typing import List
from src.domain.models.leito_model import Leito

class LeitoRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, numero_leito: str, setor_id: int, tipo: str, status: str) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, numero_leito: str, setor_id: int, tipo: str, status: str) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Leito:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Leito]:
        pass
    
    @abstractmethod
    def findByStatus(self, status: str) -> List[Leito]:
        pass
