from typing import List,Optional
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface
from src.domain.models.especialidade_model import Especialidade as EspecialidadeDomain 
class EspecialidadeRepositorySpy(EspecialidadeRepositoryInterface):
    def __init__(self):
        self.insert_especialidade_attributes = {}
        self.insert_especialidade_call_count = 0
        
        self.delete_especialidade_attributes = {}
        self.delete_especialidade_call_count = 0

        self.select_especialidade_attributes = {}
        self.select_especialidade_call_count = 0 

        self.update_especialidade_attributes = {}
        self.update_especialidade_call_count = 0 

        self.delete_especialidade_return = True
    def create(self, nome:str, descricao:str)-> None:
        self.insert_especialidade_attributes = {
            'nome':nome,
            "descricao":descricao
        }
        self.insert_especialidade_call_count+=1
    def delete(self, id:int)-> bool:
        self.delete_especialidade_attributes = {"id":id}
        self.delete_especialidade_call_count+=1 
        return self.delete_especialidade_return
    def findById(self, id:int)-> EspecialidadeDomain:
        self.select_especialidade_attributes = {"id":id}
        self.select_especialidade_call_count +=1
        especialidade = EspecialidadeDomain(
            id=id,
            nome="Especialidade Teste",
            descricao="Descrição Teste"
        )
        return especialidade
    def update(self, id: int, nome: str, descricao: str) -> None:
        self.update_especialidade_attributes = {
            'id': id,
            'nome': nome,
            'descricao': descricao
        }
        self.update_especialidade_call_count+=1
    def findAll(self)-> List[EspecialidadeDomain]:
        especialidade1 = EspecialidadeDomain(
            id=1,
            nome="Especialidade A",
            descricao="Descrição A"
        )
        especialidade2 = EspecialidadeDomain(
            descricao='Descrição B',
            id=2,
            nome='Especialidade B'
        )
        return [especialidade1,especialidade2]
    
        