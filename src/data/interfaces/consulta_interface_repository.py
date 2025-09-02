from abc import ABC, abstractmethod
from typing import List
from src.domain.models.consulta_model import Consulta

class ConsultaRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, data_hora: str, paciente_id: int, medico_id: int, especialidade_id: int, status: str, observacoes: str) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, data_hora: str, paciente_id: int, medico_id: int, especialidade_id: int, status: str, observacoes: str) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Consulta:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Consulta]:
        pass
    

