from datetime import date

class Internacao:
    def __init__(self, id: int, paciente_id: int, medico_id: int, leito_id: int, data_entrada: date, status: str):
        self.id = id
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.leito_id = leito_id
        self.data_entrada = data_entrada
        self.status = status
