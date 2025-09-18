from typing import List
from src.domain.models.financeiro_model import Financeiro as FinanceiroDomain
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface

class FinanceiroRepositorySpy(FinanceiroRepositoryInterface):
    def __init__(self):
        self.create_financeiro_attributes = {}
        self.create_financeiro_call_count = 0

        self.update_financeiro_attributes = {}
        self.update_financeiro_call_count = 0

        self.delete_financeiro_attributes = {}
        self.delete_financeiro_call_count = 0

        self.findById_financeiro_attributes = {}
        self.findById_financeiro_call_count = 0

        self.findAll_financeiro_call_count = 0

    def create(self, paciente_id: int, convenio_id: int, valor: float, data_emisao: str, data_vencimento: str, status_pagamento: str) -> None:
        self.create_financeiro_attributes = {
            "paciente_id": paciente_id,
            "convenio_id": convenio_id,
            "valor": valor,
            "data_emisao": data_emisao,
            "data_vencimento": data_vencimento,
            "status_pagamento": status_pagamento
        }
        self.create_financeiro_call_count += 1

    def update(self, id: int, paciente_id: int, convenio_id: int, valor: float, data_emisao: str, data_vencimento: str, status_pagamento: str) -> None:
        self.update_financeiro_attributes = {
            "id": id,
            "paciente_id": paciente_id,
            "convenio_id": convenio_id,
            "valor": valor,
            "data_emisao": data_emisao,
            "data_vencimento": data_vencimento,
            "status_pagamento": status_pagamento
        }
        self.update_financeiro_call_count += 1

    def delete(self, id: int) -> bool:
        self.delete_financeiro_attributes = {"id": id}
        self.delete_financeiro_call_count += 1
        return True

    def findById(self, id: int) -> FinanceiroDomain:
        self.findById_financeiro_attributes = {"id": id}
        self.findById_financeiro_call_count += 1
        # Retorno fake para teste
        return FinanceiroDomain(
            id=id,
            paciente_id=1,
            convenio_id=1,
            valor=100.0,
            data_emisao="2024-01-01",
            data_vencimento="2024-01-10",
            status_pagamento="pago"
        )

    def findAll(self) -> List[FinanceiroDomain]:
        self.findAll_financeiro_call_count += 1
        financeiro1 = FinanceiroDomain(
            id=1,
            paciente_id=1,
            convenio_id=1,
            valor=100.0,
            data_emisao="2024-01-01",
            data_vencimento="2024-01-10",
            status_pagamento="pago"
        )
        financeiro2 = FinanceiroDomain(
            id=2,
            paciente_id=2,
            convenio_id=2,
            valor=200.0,
            data_emisao="2024-02-01",
            data_vencimento="2024-02-10",
            status_pagamento="pendente"
        )
        return [financeiro1, financeiro2]