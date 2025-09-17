from typing import Dict
from src.domain.usecases.leito.insert_leito import LeitoInsertUseCase as LeitoInsertInterface
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface 
from src.infra.db.entities.leito import Leito
from src.errors.types.http_bad_request import HttpBadRequestError
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
class LeitoInsertUseCase(LeitoInsertInterface):
    def __init__(self, leito_repository: LeitoRepositoryInterface,setor_repository:SetorRepositoryInterface):

        self.leito_repository = leito_repository
        self.setor_repository = setor_repository

    def insert(self, leito: Leito) -> Dict:
        self.__validate_informations(leito=leito)
        self.__insert_leito(leito=leito)
        response = self.__format_response(leito=leito)
        return response
    def __validate_informations(self,leito:Leito)-> None:
        if leito.numero_leito < 0 or leito.numero_leito > 30:
            raise HttpBadRequestError("Número do leito inválido. Deve estar entre 0 e 30.")
        setor = self.setor_repository.findById(id=leito.setor_id)
        if not setor:
            raise HttpBadRequestError("Setor não encontrado para o ID fornecido.")
        if leito.tipo not in ['Enfermaria', 'Apartamento', 'UTI Adulto', 'UTI Neonatal', 'UTI Pediátrica']:
            raise HttpBadRequestError("tipo de leito invalido")
        if leito.status not in ['disponivel','ocupado']:
            raise HttpBadRequestError("status do leito invalido")
        return None
    def __insert_leito(self,leito:Leito)-> None:
        self.leito_repository.create(
            numero_leito=leito.numero_leito,
            setor_id=leito.setor_id,
            tipo=leito.tipo,
            status=leito.status
        ) 
        return None
    def __format_response(self,leito:Leito)-> Dict:
        response = {
            "type":"Leito",
            "id":leito.id,
            "attributes":{
                "numero_leito":leito.numero_leito,
                "setor_id":leito.setor_id,
                "tipo":leito.tipo,
                "status":leito.status
            }
        }
        return response

