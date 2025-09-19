from typing import Dict
from src.domain.usecases.setor.insert_setor import SetorInsertUseCase as SetorInsertInterface
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface 
from src.infra.db.entities.setor import Setor
from src.errors.types.http_bad_request import HttpBadRequestError
import re 
class SetorInsertUseCase(SetorInsertInterface):
    def __init__(self, setor_repository: SetorRepositoryInterface):
        self.setor_repository = setor_repository
    
    def insert(self, setor: Setor) -> Dict:
        self.__validate_informations(
            nome=setor.nome,
            andar=setor.andar,
            capacidade=setor.capacidade,
            responsavel=setor.responsavel
        ) 
        self.__insert_setor(
            nome=setor.nome,
            andar=setor.andar,
            capacidade=setor.capacidade,
            responsavel=setor.responsavel
        )
        response = self.__format_response(setor=setor)
        return response
    def __validate_informations(self,nome:str,andar:int,capacidade:int,responsavel:str)-> None:
        if len(nome) < 0 or len(nome) > 100 or re.search(r'[^a-zA-Z]', nome):
            raise HttpBadRequestError("nome invalido")
        if andar < 0 or not isinstance(andar,int):
            raise HttpBadRequestError("ansdar invalido")
        if capacidade < 0 or not isinstance(capacidade,int):
            raise HttpBadRequestError("capacidade invalida")
        if len(responsavel) < 0 or len(responsavel) > 100 or re:
            raise HttpBadRequestError("responsavel invalido")
        return None
    def __insert_setor(self,nome:str,andar:int,capacidade:int,responsavel:str)-> None:
        self.setor_repository.create(
            nome=nome,
            andar=andar,
            capacidade=capacidade,
            responsavel=responsavel
        )
        return None
    def __format_response(self,setor: Setor)-> Dict:
        response = {
            "type": "Setor",
            "id": setor.id,
            "attributes": {
                "nome": setor.nome,
                "andar": setor.andar,
                "capacidade": setor.capacidade,
                "responsavel": setor.responsavel
            }
        }
        return response