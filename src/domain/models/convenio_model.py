from typing import Optional
class Convenio:
    def __init__(self, nome: str, tipo_plano: str, id:Optional[int]=None):
        self.id = id
        self.nome = nome
        self.tipo_plano = tipo_plano
