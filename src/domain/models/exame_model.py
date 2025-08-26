from datetime import date

class Exame:
    def __init__(self, id: int, tipo_exame: str, data_exame: date, paciente_id: int, medico_id: int, resultado: str, status: str):
        self.id = id
        self.tipo_exame = tipo_exame
        self.data_exame = data_exame
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.resultado = resultado
        self.status = status
