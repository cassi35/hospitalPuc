from typing import Optional
from datetime import date

class Paciente:
    def __init__(self,nome: str, cpf: str, data_nascimento: date, sexo: str, telefone: str, contato_emergencia: str, alergia: str, endereco_id: int, convenio_id: int, id:Optional[int]=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.telefone = telefone
        self.alergia = alergia
        self.contato_emergencia = contato_emergencia
        self.endereco_id = endereco_id
        self.convenio_id = convenio_id
