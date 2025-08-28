from abc import ABC, abstractmethod
from typing import List
from src.domain.models.endereco_model import Endereco

class EnderecoRepositoryInterface(ABC):
    @abstractmethod
    def insert_endereco(self, rua: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        pass

    @abstractmethod
    def select_endereco(self, id: int) -> Endereco:
        pass

    @abstractmethod
    def delete_endereco(self, id: int) -> bool:
        pass
    @abstractmethod
    def select_all_enderecos(self) -> List[Endereco]:pass
    @abstractmethod
    def update_endereco(self, id: int, rua: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        pass
    @abstractmethod
    def find_by_cep(self, cep: str) -> List[Endereco]:
        pass