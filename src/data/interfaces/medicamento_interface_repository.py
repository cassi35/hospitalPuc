from abc import ABC, abstractmethod
from typing import List
from src.domain.models.medicamento_model import Medicamento

class MedicamentoRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, nome: str, descricao: str, fabricante: str, validade: str, quantidade_estoque: int) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, nome: str, descricao: str, fabricante: str, validade: str, quantidade_estoque: int) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Medicamento:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Medicamento]:
        pass
    
    @abstractmethod
    def findByNome(self, nome: str) -> Medicamento:
        pass
