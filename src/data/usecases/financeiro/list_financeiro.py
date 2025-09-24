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
            "id": financeiro.id,
            "attributes": {
                "paciente_id": financeiro.paciente_id,
                "convenio_id": financeiro.convenio_id,
                "valor": financeiro.valor,
                "data_emisao": financeiro.data_emisao.isoformat() if financeiro.data_emisao else None,
                "data_vencimento": financeiro.data_vencimento.isoformat() if financeiro.data_vencimento else None,
                "status_pagamento": financeiro.status_pagamento
            }
        }
        return response