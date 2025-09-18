from typing import List, Optional
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface
from src.domain.models.convenio_model import Convenio as ConvenioDomain
class ConvenioRepositorySpy(ConvenioRepositoryInterface):
    def __init__(self):
        self.insert_convenio_attributes = {}
        self.insert_convenio_call_count = 0
        
        self.delete_convenio_attributes = {}
        self.delete_convenio_call_count = 0

        self.select_convenio_attributes = {}
        self.select_convenio_call_count = 0 

        self.udpate_convenio_attributes = {}
        self.udpate_convenio_call_count = 0 

        self.delete_convenio_return = True
    def insert_convenio(self,nome:str,tipo_plano:str)->None:
        self.insert_convenio_attributes = {
            'nome': nome,
            'tipo_plano': tipo_plano
        }
        self.insert_convenio_call_count += 1
    def delete_convenio(self,id:int) -> bool:
        self.delete_convenio_attributes = {"id":id}
        self.delete_convenio_call_count+=1 
        return self.delete_convenio_return
    def select_convenio(self,id:int)-> ConvenioDomain:
        self.select_convenio_attributes = {"id":id}
        self.select_convenio_call_count +=1
        convenio = ConvenioDomain(
            id=id,
            nome="Convenio Teste",
            tipo_plano="Plano Teste"
        )
        return convenio
    def udpate_convenio(self, id:int, nome:str, tipo_plano:str)-> None:
        self.udpate_convenio_attributes = {
            'id': id,
            'nome': nome,
            'tipo_plano': tipo_plano
        }
        self.udpate_convenio_call_count+=1
    def findAll(self):
        convenio1 = ConvenioDomain(
            id=1,
            nome="Convenio A",
            tipo_plano="Plano A"
        )
        convenio2 = ConvenioDomain(
            id=2,
            nome="Convenio B",
            tipo_plano="Plano B"
        )
        return [convenio1, convenio2]
    def findByNome(self, nome:str)-> ConvenioDomain:
        convenio = ConvenioDomain(
            id=1,
            nome=nome,
            tipo_plano="Plano Teste"
        )
        return convenio