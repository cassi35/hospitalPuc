from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
from src.domain.models.setor_model import Setor as SetorDomain 
from typing import List, Optional
class SetorRepositorySpy(SetorRepositoryInterface):
    def __init__(self):
        self.insert_setor_attributes = {}
        self.insert_setor_call_count = 0
        
        self.delete_setor_attributes = {}
        self.delete_setor_call_count = 0

        self.select_setor_attributes = {}
        self.select_setor_call_count = 0 

        self.udpate_setor_attributes = {}
        self.udpate_setor_call_count = 0 

        self.delete_setor_return = True
    def create(self, nome:str, andar:int, capacidade:int, responsavel:str)-> None:
        self.insert_setor_attributes = {
            'nome': nome,
            'andar': andar,
            'capacidade': capacidade,
            'responsavel': responsavel
        }
        self.insert_setor_call_count += 1
    def delete(self, id: int) -> bool:
        self.delete_setor_attributes = {"id":id}
        self.delete_setor_call_count+=1 
        return self.delete_setor_return
    def findAll(self)-> List[SetorDomain]:
        setor1 = SetorDomain(
            id=1,
            nome="Setor A",
            andar=1,
            capacidade=10,
            responsavel="Responsável A"
        )
        setor2 = SetorDomain(
            id=2,
            nome="Setor B",
            andar=2,
            capacidade=20,
            responsavel="Responsável B"
        )
        return [setor1, setor2]
    def findByNome(self, nome:str)-> SetorDomain:
        self.select_setor_attributes = {"nome":nome}
        self.select_setor_call_count +=1
        setor = SetorDomain(
            id=1,
            nome=nome,
            andar=1,
            capacidade=10,
            responsavel="Responsável A"
        )
        return setor
    def findById(self, id:int)-> SetorDomain:
        self.select_setor_attributes = {"id":id}
        self.select_setor_call_count +=1
        setor = SetorDomain(
            id=id,
            nome="Setor Teste",
            andar=1,
            capacidade=10,
            responsavel="Responsável Teste"
        )
        return setor
    def update(self, id:int, nome:str, andar:int, capacidade:int, responsavel:str)-> None:
        self.udpate_setor_attributes = {
            'id': id,
            'nome': nome,
            'andar': andar,
            'capacidade': capacidade,
            'responsavel': responsavel
        }
        self.udpate_setor_call_count+=1
