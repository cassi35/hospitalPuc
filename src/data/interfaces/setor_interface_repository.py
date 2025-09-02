from abc import ABC, abstractmethod
from typing import List
from src.domain.models.setor_model import Setor

class SetorRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, nome: str, andar: int, capacidade: int, responsavel: str) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, nome: str, andar: int, capacidade: int, responsavel: str) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Setor:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Setor]:
        pass
    
    @abstractmethod
    def findByNome(self, nome: str) -> Setor:
        pass
