from typing import Optional
class Especialidade:
    def __init__(self, nome: str, descricao: str, id:Optional[int]=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
