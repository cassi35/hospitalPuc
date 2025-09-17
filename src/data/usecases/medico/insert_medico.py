from typing import Dict
from src.domain.usecases.medico.insert_medico import MedicoInsertUseCase as MedicoInsertInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface 
from src.infra.db.entities.medico import Medico
from src

class MedicoInsertUseCase(MedicoInsertInterface):
    def __init__(self, medico_repository: MedicoRepositoryInterface):
        self.medico_repository = medico_repository
    
    def insert(self, medico: Medico) -> Dict:
        pass
    def __validate_informations(self,nome:str,cpf:str,especialidade_id:int,telefone:str,email:str,status:str)-> None:
        pass 
    def __insert_medico(self,nome:str,cpf:str,especialidade_id:int,telefone:str,email:str,status:str)-> None:
        pass
    def __format_response(self,nome:str,cpf:str,especialidade_id:int,telefone:str,email:str,status:str) -> Dict:
        response = {
            "type":"Medico",
            "count":1,
            "attributes":{
                "nome": nome,
                "cpf": cpf,
                "especialidade_id": especialidade_id,
                "telefone": telefone,
                "email": email,
                "status": status
            }
        } 
        return response