from src.domain.usecases.internacao.delete_internacao import InternacaoDeleteUseCase as InternacaoDeleteInterface
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from typing import Dict

class InternacaoDeleteUseCase(InternacaoDeleteInterface):
    def __init__(self, internacao_repository: InternacaoRepositoryInterface):
        self.internacao_repository = internacao_repository

    def delete(self, internacao_id: int) -> Dict:
        self.__validate_internacao_id(internacao_id)
        self.__exists_internacao(internacao_id)
        self.internacao_repository.delete(internacao_id)
        return self.__format_response(internacao_id)

    def __validate_internacao_id(self, internacao_id: int) -> None:
        if not isinstance(internacao_id, int) or internacao_id <= 0:
            raise HttpBadRequestError("ID da internação deve ser um número positivo")

    def __exists_internacao(self, internacao_id: int) -> None:
        if not self.internacao_repository.findById(internacao_id):
            raise HttpNotFoundError("Internação não encontrada")

    def __format_response(self, internacao_id: int) -> Dict:
        return {
            "type": "Internacao",
            "id": internacao_id,
            "deleted": True
        }