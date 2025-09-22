from typing import Optional
from datetime import date

class Consulta:
    def __init__(self, data_hora: date, paciente_id: int, medico_id: int, especialidade_id: int, status: str, observacoes: str, id:Optional[int]=None):
        self.id = id
        self.data_hora = data_hora
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.especialidade_id = especialidade_id
        self.status = status
        self.observacoes = observacoes
