from typing import Optional
from datetime import date

class Funcionario:
    def __init__(self, nome: str, cpf: str, cargo: str, setor_id: int, telefone: str, email: str, data_contratacao: date, id:Optional[int]=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.setor_id = setor_id
        self.telefone = telefone
        self.email = email
        self.data_contratacao = data_contratacao
