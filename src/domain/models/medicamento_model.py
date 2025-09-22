from typing import Optional
from datetime import date

class Medicamento:
    def __init__(self, nome: str, descricao: str, fabricante: str, validade: date, quantidade_estoque: int, id:Optional[int]=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.fabricante = fabricante
        self.validade = validade
        self.quantidade_estoque = quantidade_estoque
