from typing import Dict
from src.domain.usecases.especialidade.update_especialidade import EspecialidadeUpdateUseCase as EspecialidadeUpdateInterface
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface 
from src.infra.db.entities.especialidade import Especialidade
from src.errors.types.http_bad_request import HttpBadRequestError
class EspecialidadeUpdateUseCase(EspecialidadeUpdateInterface):
    def __init__(self, especialidade_repository: EspecialidadeRepositoryInterface):
        self.especialidade_repository = especialidade_repository
        
    def update(self, especialidade_id: int, especialidade: Especialidade) -> Dict:
        self.__validate_informations(
            especialidade_id=especialidade_id,
            descricao=especialidade.descricao,
            nome=especialidade.nome
        )
        self.__update_especialidade(
            especialidade_id=especialidade_id,
            descricao=especialidade.descricao,
            nome=especialidade.nome
        )
        response = self.__format_response(
            especialidade_id=especialidade_id,
            descricao=especialidade.descricao,
            nome=especialidade.nome
        )
        return response
    def __validate_informations(self,especialidade_id:int,nome:str,descricao:str)-> None:
        if not especialidade_id or especialidade_id <= 0:
            raise HttpBadRequestError("id invalido")
        if not self.especialidade_repository.findById(id=especialidade_id):
            raise HttpBadRequestError("especialidade nao encontrada")
        if not nome or nome.strip() == "" or  ( len(nome) > 50 or len(nome) < 3):
            raise  HttpBadRequestError("nome invalido")
        if not descricao or descricao.strip() == "" or (len(descricao) > 200 or len(descricao) < 5):
            raise HttpBadRequestError("descricao invalido")
        return None
    def __update_especialidade(self,especialidade_id:int,nome:str,descricao:str) -> None:
        self.especialidade_repository.update(
            descricao=descricao,
             id=especialidade_id,
             nome=nome
        )
        return None
    def __format_response(self,especialidade_id:int , nome:str,descricao:str) -> Dict:
        response = {
            "type":"Especialidade",
            "count":1,
            "attributes":{
                "id": especialidade_id,
                "nome": nome,
                "descricao": descricao
            }
        } 
        return response