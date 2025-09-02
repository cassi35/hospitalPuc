from abc import ABC, abstractmethod
from typing import List
from src.domain.models.prescricao_model import Prescricao

class PrescricaoRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, paciente_id: int, medico_id: int, data_prescricao: str, medicamento_id: int, dosagem: int, frequencia: int) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, paciente_id: int, medico_id: int, data_prescricao: str, medicamento_id: int, dosagem: int, frequencia: int) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Prescricao:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Prescricao]:
        pass
