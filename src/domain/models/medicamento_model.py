from datetime import date

class Medicamento:
    def __init__(self, id: int, nome: str, descricao: str, fabricante: str, validade: date, quantidade_estoque: int):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.fabricante = fabricante
        self.validade = validade
        self.quantidade_estoque = quantidade_estoque
