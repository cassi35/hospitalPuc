from typing import Optional
from datetime import date

class Prescricao:
    def __init__(self,  paciente_id: int, medico_id: int, data_prescricao: date, medicamento_id: int, dosagem: int, frequencia: int, id:Optional[int]=None):
        self.id = id
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.data_prescricao = data_prescricao
        self.medicamento_id = medicamento_id
        self.dosagem = dosagem
        self.frequencia = frequencia
