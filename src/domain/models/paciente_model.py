from datetime import date

class Paciente:
    def __init__(self, id: int, nome: str, cpf: str, data_nascimento: date, sexo: str, telefone: str, contato_emergencia: str, alergia: str, endereco_id: int, convenio_id: int):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.telefone = telefone
        self.contato_emergencia = contato_emergencia
        self.alergia = alergia
        self.endereco_id = endereco_id
        self.convenio_id = convenio_id
