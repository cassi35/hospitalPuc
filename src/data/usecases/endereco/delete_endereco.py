from src.domain.usecases.endereco.delete_endereco import EnderecoDeleteUseCase as EnderecoDeleteInterface
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface
from typing import Dict
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_bad_request import HttpBadRequestError
from typing import Dict

class EnderecoDeleteUseCase(EnderecoDeleteInterface):
    def __init__(self, endereco_repository: EnderecoRepositoryInterface):
        self.endereco_repository = endereco_repository

    def delete(self, endereco_id: int) -> Dict:
        # Valida se o ID é válido
        self._validate_endereco_id(endereco_id)
        
        # Verifica se o endereço existe
        self._exists_endereco(endereco_id=endereco_id)
        
        # Deleta o endereço
        self.endereco_repository.delete_endereco(endereco_id=endereco_id)
        
        # Retorna resposta de sucesso
        return {
            "type": "Endereco",
            "count": 1,
            "attributes": {
                "id": endereco_id,
                "deleted": True
            }
        }

    def _validate_endereco_id(self, endereco_id: int) -> Dict:
        if not isinstance(endereco_id, int) or endereco_id <= 0:
            raise HttpBadRequestError("ID do endereco deve ser um numero positivo")

    def _exists_endereco(self, endereco_id: int) -> Dict:
        endereco = self.endereco_repository.select_endereco(endereco_id)  # Corrigido parâmetro
        if not endereco:
            raise HttpNotFoundError("endereco nao encontrado")