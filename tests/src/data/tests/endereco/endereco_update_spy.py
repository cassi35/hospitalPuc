from typing import Dict
from src.infra.db.entities.endereco import Endereco
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface

class EnderecoUpdateSpy(EnderecoRepositoryInterface):
    def __init__(self) -> None:
        self.update_endereco_attributes = {}
        self.update_endereco_call_count = 0

    def update_endereco(self, endereco_id: int, endereco: Endereco) -> None:
        self.update_endereco_attributes = vars(endereco)
        self.update_endereco_attributes['id'] = endereco_id
        self.update_endereco_call_count += 1
