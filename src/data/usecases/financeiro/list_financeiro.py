from typing import List, Dict
from src.domain.usecases.financeiro.list_financeiro import FinanceiroListUseCase as FinanceiroListInterface
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface
from src.domain.models.financeiro_model import Financeiro

class FinanceiroListUseCase(FinanceiroListInterface):
    def __init__(self, financeiro_repository: FinanceiroRepositoryInterface):
        self.financeiro_repository = financeiro_repository
    
    def list(self) -> List[Dict]:
        financeiros = self.financeiro_repository.findAll()
        return [self.__format_response(fin) for fin in financeiros]
    
    def __format_response(self, financeiro: Financeiro) -> Dict:
        response = {
            "type": "Financeiro",
            "id": getattr(financeiro, "id", None),
            "attributes": {
                "paciente_id": getattr(financeiro, "paciente_id", None),
                "convenio_id": getattr(financeiro, "convenio_id", None),
                "valor": getattr(financeiro, "valor", None),
                "data_emisao": getattr(financeiro, "data_emisao", None),
                "data_vencimento": getattr(financeiro, "data_vencimento", None),
                "status_pagamento": getattr(financeiro, "status_pagamento", None)
            }
        }
        return response