from typing import Dict
from src.domain.usecases.setor.update_setor import SetorUpdateUseCase as SetorUpdateInterface
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface 
from src.domain.models.setor_model import Setor
from src.errors.types.http_bad_request import HttpBadRequestError
import re 
class SetorUpdateUseCase(SetorUpdateInterface):
    def __init__(self, setor_repository: SetorRepositoryInterface):
        self.setor_repository = setor_repository
    
    def update(self, setor_id: int, setor: Setor) -> Dict:
        self.__validate_informations(
            nome=setor.nome,
            andar=setor.andar,
            capacidade=setor.capacidade,
            responsavel=setor.responsavel
        )
        self.__setor_exists(id=setor_id)
        self.__update_setor(setor=setor)
        response = self.__format_response(setor=setor)
        return response
    def __validate_informations(self,nome:str,andar:int,capacidade:int,responsavel:str)-> None:
        if len(nome) < 0 or len(nome) > 100 or re.search(r'[^a-zA-Z]', nome):
            raise HttpBadRequestError("nome invalido")
        if andar < 0 or not isinstance(andar,int):
            raise HttpBadRequestError("andar invalido")
        if capacidade < 0 or not isinstance(capacidade,int):
            raise HttpBadRequestError("capacidade invalida")
        if len(responsavel) < 0 or len(responsavel) > 100 or re.search(r'[^a-zA-Z]', responsavel):
            raise HttpBadRequestError("responsavel invalido")
        return None
    def __setor_exists(self,id:int)-> None:
        setor = self.setor_repository.findById(id=id)
        if not setor:
            raise HttpBadRequestError("setor nao encontrado")
        return None 
         
    def __update_setor(self,setor:Setor)-> None:
        self.setor_repository.update(
            id=setor.id,
            nome=setor.nome,
            andar=setor.andar,
            capacidade=setor.capacidade,
            responsavel=setor.responsavel
        )
        return None
    def __format_response(self,setor:Setor)-> Dict:
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