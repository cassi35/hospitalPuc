from typing import List, Dict
from src.domain.usecases.leito.list_leito import LeitoListUseCase as LeitoListInterface
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface
from src.infra.db.entities.leito import Leito
class LeitoListUseCase(LeitoListInterface):
    def __init__(self, leito_repository: LeitoRepositoryInterface):
        self.leito_repository = leito_repository
    
    def list(self) -> List[Dict]:
        leitos = self.leito_repository.findAll()
        response = [self.__list_format_response(leito) for leito in leitos]
        return response

    def __list_format_response(self,leito:Leito) -> Dict:
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
