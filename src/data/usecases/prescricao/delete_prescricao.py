from typing import Dict
from src.domain.usecases.prescricao.delete_prescricao import PrescricaoDeleteUseCase as PrescricaoDeleteInterface
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError

class PrescricaoDeleteUseCase(PrescricaoDeleteInterface):
    def __init__(self, prescricao_repository: PrescricaoRepositoryInterface):
        self.prescricao_repository = prescricao_repository

    def delete(self, prescricao_id: int) -> Dict:
        self.__validate_prescricao_id(prescricao_id)
        self.__exists_prescricao(prescricao_id)
        self.__delete_prescricao(prescricao_id)
        return self.__format_response(prescricao_id)

    def __validate_prescricao_id(self, prescricao_id: int) -> None:
        if not isinstance(prescricao_id, int) or prescricao_id <= 0:
            raise HttpBadRequestError("ID da prescrição deve ser um número positivo")

    def __exists_prescricao(self, prescricao_id: int) -> None:
        prescricao = self.prescricao_repository.findById(prescricao_id)
        if not prescricao:
            raise HttpNotFoundError("Prescrição não encontrada")

    def __delete_prescricao(self, prescricao_id: int) -> None:
        self.prescricao_repository.delete(prescricao_id)

    def __format_response(self, prescricao_id: int) -> Dict:
        return {
            "type": "Prescricao",
            "count": 1,
            "attributes": {
                "id": prescricao_id,
                "deleted": True
            }
        }