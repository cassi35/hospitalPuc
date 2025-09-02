from abc import ABC, abstractmethod
from typing import List
from src.domain.models.exame_model import Exame

class ExameRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, tipo_exame: str, data_exame: str, paciente_id: int, medico_id: int, resultado: str, status: str) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, tipo_exame: str, data_exame: str, paciente_id: int, medico_id: int, resultado: str, status: str) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Exame:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Exame]:
        pass
