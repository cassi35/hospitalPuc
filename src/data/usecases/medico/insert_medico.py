from typing import Dict
from src.domain.usecases.medico.insert_medico import MedicoInsertUseCase as MedicoInsertInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface 
from src.infra.db.entities.medico import Medico
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
import re 
class MedicoInsertUseCase(MedicoInsertInterface):
    def __init__(self, medico_repository: MedicoRepositoryInterface,especialidade_repository:EspecialidadeRepositoryInterface):
        self.medico_repository = medico_repository
        self.especialidade_repository = especialidade_repository
    def insert(self, medico: Medico) -> Dict:
        self.__validate_informations(
            status=medico.status,
            nome=medico.nome,
            cpf=medico.cpf,
            especialidade_id=medico.especialidade_id,
            telefone=medico.telefone,
            email=medico.email
        )
        self.__insert_medico(
            status=medico.status,
            nome=medico.nome,
            cpf=medico.cpf,
            especialidade_id=medico.especialidade_id,
            telefone=medico.telefone,
            email=medico.email
        )
        response = self.__format_response(
            status=medico.status,
            nome=medico.nome,
            cpf=medico.cpf,
            especialidade_id=medico.especialidade_id,
            telefone=medico.telefone,
            email=medico.email
        )
        return response
    def __validate_informations(self,nome:str,cpf:str,especialidade_id:int,telefone:str,email:str,status:str)-> None:
        if len(cpf) != 11 or self.medico_repository.findByCpf(cpf=cpf) != None:
            raise   HttpBadRequestError("cpf invalido ou ja cadastrado")
        if self.especialidade_repository.findById(id=especialidade_id) != None or especialidade_id <= 0 or not isinstance(especialidade_id,int):
            raise HttpBadRequestError("especialidade_id invalido ou nao cadastrado")
        if len(telefone) != 9:
            raise HttpBadRequestError("telefone invalido")
        if status not in ['ativo','nao ativo']:
            raise HttpBadRequestError("status invalido")
        if len(nome)> 20 or len(nome) == 0:
            raise HttpBadRequestError("nome invalido")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None or len(email) == 0 :

            raise HttpBadRequestError("email invalido")
        return None
    def __insert_medico(self,nome:str,cpf:str,especialidade_id:int,telefone:str,email:str,status:str)-> None:
        self.medico_repository.create(
            email=email,
            nome=nome,
            cpf=cpf,
            especialidade_id=especialidade_id,
            telefone=telefone,
            status=status
        )
        return None
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