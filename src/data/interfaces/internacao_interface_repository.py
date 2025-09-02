from abc import ABC, abstractmethod
from typing import List
from src.domain.models.internacao_model import Internacao

class InternacaoRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, paciente_id: int, medico_id: int, leito_id: int, data_entrada: str, status: str) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, paciente_id: int, medico_id: int, leito_id: int, data_entrada: str, status: str) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Internacao:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Internacao]:
        pass
