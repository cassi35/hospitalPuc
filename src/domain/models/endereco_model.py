from typing import Optional
class Endereco:
    def __init__(self,rua:str,bairro:str,cidade:str,estado:str,cep:str, id:Optional[int]=None):
        self.id = id
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep=cep