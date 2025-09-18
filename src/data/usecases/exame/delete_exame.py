from typing import Dict
from src.domain.usecases.exame.delete_exame import ExameDeleteUseCase as ExameDeleteInterface
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError

class ExameDeleteUseCase(ExameDeleteInterface):
    def __init__(self, exame_repository: ExameRepositoryInterface):
        self.exame_repository = exame_repository

    def delete(self, exame_id: int) -> Dict:
        self.__validate_id(exame_id)
        self.__exists(exame_id)
        self.exame_repository.delete(exame_id)
        return self.__format_response(exame_id)

    def __validate_id(self, exame_id: int) -> None:
        if not isinstance(exame_id, int) or exame_id <= 0:
            raise HttpBadRequestError("ID inválido")

    def __exists(self, exame_id: int) -> None:
        if not self.exame_repository.findById(exame_id):
            raise HttpNotFoundError("Exame não encontrado")

    def __format_response(self, exame_id: int) -> Dict:
        return {
            "type": "Exame",
            "id": exame_id,
            "deleted": True
        }