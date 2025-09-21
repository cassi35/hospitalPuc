from typing import Dict
from src.domain.usecases.especialidade.insert_especialidade import EspecialidadeInsertUseCase as EspecialidadeInsertInterface
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface 
from src.infra.db.entities.especialidade import Especialidade
from src.errors.types.http_bad_request import HttpBadRequestError
class EspecialidadeInsertUseCase(EspecialidadeInsertInterface):
    def __init__(self, especialidade_repository: EspecialidadeRepositoryInterface):
        self.especialidade_repository = especialidade_repository
    
    def insert(self, especialidade: Especialidade) -> Dict:
        self.__validate_informations(descricao=especialidade.descricao,nome=especialidade.nome)
        self.__insert_especialidade(descricao=especialidade.descricao,nome=especialidade.nome)
        response = self.__format_response(descricao=especialidade.descricao,nome=especialidade.nome)
        return response
    def __validate_informations(self,nome:str,descricao:str)-> None:
        if not nome or nome.strip() == "" or  ( len(nome) > 50 or len(nome) < 3) or not nome.isalpha():
            raise  HttpBadRequestError("nome invalido")
        if not descricao or descricao.strip() == "" or (len(descricao) > 200 or len(descricao) < 5) or not descricao.isalpha():
            raise HttpBadRequestError("descricao invalido")
        return None
    def __insert_especialidade(self,nome:str,descricao:str)-> None:
        self.especialidade_repository.create(nome=nome,descricao=descricao)
        return None
    def __format_response(self,nome:str,descricao:str) -> Dict:
        response = {
            "type":"Especialidade",
            "count":1,
            "attributes":{
                "nome": nome,
                "descricao": descricao
            }
        } 
        return response
