class Medico:
    def __init__(self, id: int, nome: str, cpf: str, especialidade_id: int, telefone: str, email: str, status: str):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.especialidade_id = especialidade_id
        self.telefone = telefone
        self.email = email
        self.status = status
