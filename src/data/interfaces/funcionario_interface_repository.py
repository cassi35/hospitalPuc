from abc import ABC, abstractmethod
from typing import List
from src.domain.models.funcionario_model import Funcionario

class FuncionarioRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, nome: str, cpf: str, cargo: str, setor_id: int, telefone: str, email: str, data_contratacao: str) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, nome: str, cpf: str, cargo: str, setor_id: int, telefone: str, email: str, data_contratacao: str) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Funcionario:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Funcionario]:
        pass

