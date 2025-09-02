from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface
from src.domain.models.financeiro_model import Financeiro as FinanceiroDomain
from src.infra.db.entities.financeiro import Financeiro as FinanceiroEntity

class FinanceiroRepository(FinanceiroRepositoryInterface):
    
    def create(self, paciente_id: int, convenio_id: int, valor: float, data_emisao: str, data_vencimento: str, status_pagamento: str) -> None:
        pass
    
    def update(self, id: int, paciente_id: int, convenio_id: int, valor: float, data_emisao: str, data_vencimento: str, status_pagamento: str) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> FinanceiroDomain:
        pass
    
    def findAll(self) -> List[FinanceiroDomain]:
        pass
    
    def findByPaciente(self, paciente_id: int) -> List[FinanceiroDomain]:
        pass
    
    def findByConvenio(self, convenio_id: int) -> List[FinanceiroDomain]:
        pass
    
    def findByStatus(self, status_pagamento: str) -> List[FinanceiroDomain]:
        pass
