from typing import Dict
from src.domain.usecases.financeiro.delete_financeiro import FinanceiroDeleteUseCase as FinanceiroDeleteInterface
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError

class FinanceiroDeleteUseCase(FinanceiroDeleteInterface):
    def __init__(self, financeiro_repository: FinanceiroRepositoryInterface):
        self.financeiro_repository = financeiro_repository
    
    def delete(self, financeiro_id: int) -> Dict:
        self.__validate_id(financeiro_id)
        self.__exists(financeiro_id)
        self.financeiro_repository.delete(financeiro_id)
        return self.__format_response(financeiro_id)

    def __validate_id(self, financeiro_id: int) -> None:
        if not isinstance(financeiro_id, int) or financeiro_id <= 0:
            raise HttpBadRequestError("ID inválido")

    def __exists(self, financeiro_id: int) -> None:
        if not self.financeiro_repository.findById(financeiro_id):
            raise HttpNotFoundError("Financeiro não encontrado")

    def __format_response(self, financeiro_id: int) -> Dict:
        return {
            "type": "Financeiro",
            "id": financeiro_id,
            "deleted": True
        }