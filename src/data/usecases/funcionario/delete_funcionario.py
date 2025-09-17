from typing import Dict

from src.domain.usecases.funcionario.delete_funcionario import FuncionarioDeleteUseCase as FuncionarioDeleteInterface
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError

class FuncionarioDeleteUseCase(FuncionarioDeleteInterface):
    def __init__(self, funcionario_repository: FuncionarioRepositoryInterface):
        self.funcionario_repository = funcionario_repository

    def delete(self, funcionario_id: int) -> Dict:
        self.__validate_id(funcionario_id)
        self.__exists(funcionario_id)
        self.funcionario_repository.delete(funcionario_id)
        return self.__format_response(funcionario_id)

    def __validate_id(self, funcionario_id: int) -> None:
        if not isinstance(funcionario_id, int) or funcionario_id <= 0:
            raise HttpBadRequestError("ID inválido")

    def __exists(self, funcionario_id: int) -> None:
        if not self.funcionario_repository.findById(funcionario_id):
            raise HttpNotFoundError("Funcionário não encontrado")

    def __format_response(self, funcionario_id: int) -> Dict:
        return {
            "type": "Funcionario",
            "id": funcionario_id,
            "deleted": True
        }