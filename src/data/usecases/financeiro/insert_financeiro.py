from typing import Dict
from datetime import datetime
from src.domain.usecases.financeiro.insert_financeiro import FinanceiroInsertUseCase as FinanceiroInsertInterface
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface
from src.domain.models.financeiro_model import Financeiro
from src.errors.types.http_bad_request import HttpBadRequestError

class FinanceiroInsertUseCase(FinanceiroInsertInterface):
    def __init__(
        self,
        financeiro_repository: FinanceiroRepositoryInterface,
        paciente_repository: PacienteRepositoryInterface,
        convenio_repository: ConvenioRepositoryInterface
    ):
        self.financeiro_repository = financeiro_repository
        self.paciente_repository = paciente_repository
        self.convenio_repository = convenio_repository
    
    def insert(self, financeiro: Financeiro) -> Dict:
        self.__validate_informations(financeiro)
        # create(paciente_id, convenio_id, valor, data_emisao, data_vencimento, status_pagamento)
        self.financeiro_repository.create(
            financeiro.paciente_id,
            financeiro.convenio_id,
            financeiro.valor,
            financeiro.data_emisao,
            financeiro.data_vencimento,
            financeiro.status_pagamento
        )
        return self.__format_response(financeiro)

    def __validate_informations(self, financeiro: Financeiro) -> None:
        # paciente_id
        if not isinstance(financeiro.paciente_id, int) or financeiro.paciente_id <= 0:
            raise HttpBadRequestError("paciente_id inválido")
        if not self.paciente_repository.select_paciente(financeiro.paciente_id):
            raise HttpBadRequestError("Paciente não encontrado")
        # convenio_id
        if not isinstance(financeiro.convenio_id, int) or financeiro.convenio_id <= 0:
            raise HttpBadRequestError("convenio_id inválido")
        if not self.convenio_repository.select_convenio(financeiro.convenio_id):
            raise HttpBadRequestError("Convênio não encontrado")
        # valor
        if financeiro.valor is None:
            raise HttpBadRequestError("valor é obrigatório")
        try:
            if float(financeiro.valor) <= 0:
                raise HttpBadRequestError("valor deve ser maior que 0")
        except Exception:
            raise HttpBadRequestError("valor inválido")
        # datas
        if not financeiro.data_emisao:
            raise HttpBadRequestError("data_emisao é obrigatória")
        if not financeiro.data_vencimento:
            raise HttpBadRequestError("data_vencimento é obrigatória")
        emis = self.__parse_date(financeiro.data_emisao, "data_emisao")
        venc = self.__parse_date(financeiro.data_vencimento, "data_vencimento")
        if emis > datetime.now().date():
            raise HttpBadRequestError("data_emisao não pode ser futura")
        if venc < emis:
            raise HttpBadRequestError("data_vencimento deve ser maior ou igual a data_emisao")
        # status_pagamento
        if financeiro.status_pagamento not in ["pago", "pendente", "cancelado"]:
            raise HttpBadRequestError("status_pagamento inválido")

    def __parse_date(self, value, field: str):
        try:
            return datetime.strptime(str(value), "%Y-%m-%d").date()
        except ValueError:
            raise HttpBadRequestError(f"{field} inválida")

    def __format_response(self, financeiro: Financeiro) -> Dict:
        return {
            "type": "Financeiro",
            "count": 1,
            "attributes": {
                "paciente_id": financeiro.paciente_id,
                "convenio_id": financeiro.convenio_id,
                "valor": financeiro.valor,
                "data_emisao": str(financeiro.data_emisao),
                "data_vencimento": str(financeiro.data_vencimento),
                "status_pagamento": financeiro.status_pagamento
            }
        }