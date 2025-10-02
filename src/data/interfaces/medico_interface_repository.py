from abc import ABC, abstractmethod
from typing import List
from src.domain.models.medico_model import Medico

class MedicoRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, nome: str, cpf: str, especialidade_id: int, telefone: str, email: str, status: str) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, nome: str, cpf: str, especialidade_id: int, telefone: str, email: str, status: str) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Medico:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Medico]:
        pass
    
    @abstractmethod
    def findByCpf(self, cpf: str) -> Medico:
        pass
    @abstractmethod
    def findByEmail(self,email:str)-> Medico:pass