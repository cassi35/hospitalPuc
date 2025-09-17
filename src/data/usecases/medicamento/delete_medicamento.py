from typing import Dict
from src.domain.usecases.medicamento.delete_medicamento import MedicamentoDeleteUseCase as MedicamentoDeleteInterface
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError

class MedicamentoDeleteUseCase(MedicamentoDeleteInterface):
    def __init__(self, medicamento_repository: MedicamentoRepositoryInterface):
        self.medicamento_repository = medicamento_repository

    def delete(self, medicamento_id: int) -> Dict:
        self.__validate_medicamento_id(medicamento_id)
        self.__exists_medicamento(medicamento_id)
        self.__delete_medicamento(medicamento_id)
        return self.__format_response(medicamento_id)

    def __validate_medicamento_id(self, medicamento_id: int) -> None:
        if not isinstance(medicamento_id, int) or medicamento_id <= 0:
            raise HttpBadRequestError("ID do medicamento deve ser um número positivo")

    def __exists_medicamento(self, medicamento_id: int) -> None:
        medicamento = self.medicamento_repository.findById(medicamento_id)
        if not medicamento:
            raise HttpNotFoundError("Medicamento não encontrado")

    def __delete_medicamento(self, medicamento_id: int) -> None:
        self.medicamento_repository.delete(medicamento_id)

    def __format_response(self, medicamento_id: int) -> Dict:
        return {
            "type": "Medicamento",
            "count": 1,
            "attributes": {
                "id": medicamento_id,
                "deleted": True
            }
        }