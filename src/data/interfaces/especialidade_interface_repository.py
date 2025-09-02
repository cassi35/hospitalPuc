from abc import ABC, abstractmethod
from typing import List
from src.domain.models.especialidade_model import Especialidade

class EspecialidadeRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, nome: str, descricao: str) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, nome: str, descricao: str) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Especialidade:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Especialidade]:
        pass
