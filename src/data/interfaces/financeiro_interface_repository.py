from abc import ABC, abstractmethod
from typing import List
from src.domain.models.financeiro_model import Financeiro

class FinanceiroRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, paciente_id: int, convenio_id: int, valor: float, data_emisao: str, data_vencimento: str, status_pagamento: str) -> None:
        pass
    
    @abstractmethod
    def update(self, id: int, paciente_id: int, convenio_id: int, valor: float, data_emisao: str, data_vencimento: str, status_pagamento: str) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> Financeiro:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Financeiro]:
        pass
    

