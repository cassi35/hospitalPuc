from typing import Optional
from datetime import date

class Financeiro:
    def __init__(self,  paciente_id: int, convenio_id: int, valor: float, data_emissao: date, data_vencimento: date, status_pagamento: str, id:Optional[int]=None):
        self.id = id
        self.paciente_id = paciente_id
        self.convenio_id = convenio_id
        self.valor = valor
        self.data_emissao = data_emissao
        self.data_vencimento = data_vencimento
        self.status_pagamento = status_pagamento
