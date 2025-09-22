from typing import Optional
class Leito:
    def __init__(self,  numero_leito: str, setor_id: int, tipo: str, status: str, id:Optional[int]=None):
        self.id = id
        self.numero_leito = numero_leito
        self.setor_id = setor_id
        self.tipo = tipo
        self.status = status
