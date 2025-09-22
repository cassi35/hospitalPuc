from typing import Optional
class Setor:
    def __init__(self,  nome: str, andar: int, capacidade: int, responsavel: str, id:Optional[int]=None):
        self.id = id
        self.nome = nome
        self.andar = andar
        self.capacidade = capacidade
        self.responsavel = responsavel
