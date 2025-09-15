from typing import Dict
from src.infra.db.entities.endereco import Endereco
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface

class EnderecoInsertSpy(EnderecoRepositoryInterface):
    def __init__(self) -> None:
        self.insert_endereco_attributes = {}
        self.insert_endereco_call_count = 0

    def insert_endereco(self, endereco: Endereco) -> None:
        self.insert_endereco_attributes = vars(endereco)
        self.insert_endereco_call_count += 1
