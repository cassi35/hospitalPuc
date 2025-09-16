from src.domain.usecases.convenio.delete_convenio import ConvenioDeleteUseCase as ConvenioDeleteInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from typing import Dict

class ConvenioDeleteUseCase(ConvenioDeleteInterface):
    def __init__(self, convenio_repository: ConvenioRepositoryInterface):
        self.convenio_repository = convenio_repository
    
    def delete(self, convenio_id: int) -> Dict:
        self.__validate_convenio_id(convenio_id=convenio_id)
        self.__exists_convenio(convenio_id=convenio_id)
        self.__delete_convenio(convenio_id=convenio_id)
        response = self.__format_response(convenio_id=convenio_id)
        return response
    def __validate_convenio_id(self,convenio_id:int) -> None:
        if convenio_id <= 0:
            raise HttpBadRequestError("ID de convênio inválido")
        return None
    def __exists_convenio(self,convenio_id:int)-> None:
        convenio = self.convenio_repository.select_convenio(id=convenio_id)
        if not convenio:
            raise HttpBadRequestError("convênio não encontrado")
        return None
    def __delete_convenio(self,convenio_id:int) -> None:
        self.convenio_repository.delete_convenio(id=convenio_id)
        return None
    def __format_response(self,convenio_id:int)-> Dict:
        response = {
            "type":"Convênio",
            "count":1,
            "attributes":{
                "id":convenio_id,
                "deleted":True
            }
        }
        return response