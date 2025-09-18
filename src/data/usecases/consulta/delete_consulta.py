# ...existing code...
from typing import Dict
from src.domain.usecases.consulta.delete_consulta import ConsultaDeleteUseCase as ConsultaDeleteInterface
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError

class ConsultaDeleteUseCase(ConsultaDeleteInterface):
    def __init__(self, consulta_repository: ConsultaRepositoryInterface):
        self.consulta_repository = consulta_repository

    def delete(self, consulta_id: int) -> Dict:
        self.__validate_id(consulta_id)
        self.__exists(consulta_id)
        self.consulta_repository.delete(consulta_id)
        return self.__format_response(consulta_id)

    def __validate_id(self, consulta_id: int) -> None:
        if not isinstance(consulta_id, int) or consulta_id <= 0:
            raise HttpBadRequestError("ID inválido")

    def __exists(self, consulta_id: int) -> None:
        if not self.consulta_repository.findById(consulta_id):
            raise HttpNotFoundError("Consulta não encontrada")

    def __format_response(self, consulta_id: int) -> Dict:
        return {
            "type": "Consulta",
            "id": consulta_id,
            "deleted": True
        }