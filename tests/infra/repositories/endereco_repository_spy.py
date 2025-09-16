from typing import List, Optional
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface
from src.infra.db.entities.endereco import Endereco

class EnderecoRepositorySpy(EnderecoRepositoryInterface):
    def __init__(self):
        # Tracking insert calls
        self.insert_endereco_attributes = {}
        self.insert_endereco_call_count = 0
        
        # Tracking select calls
        self.select_endereco_attributes = {}
        self.select_endereco_call_count = 0
        
        # Tracking update calls
        self.update_endereco_attributes = {}
        self.update_endereco_call_count = 0
        
        # Tracking delete calls
        self.delete_endereco_attributes = {}
        self.delete_endereco_call_count = 0

    def insert_endereco(self, rua: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        self.insert_endereco_attributes = {
            'rua': rua,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado,
            'cep': cep
        }
        self.insert_endereco_call_count += 1

    def select_endereco(self, endereco_id: int) -> Optional[Endereco]:
        self.select_endereco_attributes = {'id': endereco_id}
        self.select_endereco_call_count += 1
        
        # Retorna um endereço fake para teste
        return Endereco(
            id=endereco_id,
            rua='Rua Fake',
            bairro='Bairro Fake',
            cidade='Cidade Fake',
            estado='Estado Fake',
            cep='12345678'
        )

    def update_endereco(self, endereco_id: int, rua: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        self.update_endereco_attributes = {
            'id': endereco_id,
            'rua': rua,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado,
            'cep': cep
        }
        self.update_endereco_call_count += 1

    def delete_endereco(self, endereco_id: int) -> None:
        self.delete_endereco_attributes = {'id': endereco_id}
        self.delete_endereco_call_count += 1

    def find_by_cep(self, cep: str) -> Optional[Endereco]:
        return Endereco(
            id=99,
            rua='Rua do CEP',
            bairro='Bairro do CEP',
            cidade='Cidade do CEP',
            estado='Estado do CEP',
            cep=cep
        )
    def select_all_enderecos(self) -> List[Endereco]:
        return [
            Endereco(
                id=1,
                rua='Rua 1',
                bairro='Bairro 1',
                cidade='Cidade 1',
                estado='Estado 1',
                cep='11111111'
            ),
            Endereco(
                id=2,
                rua='Rua 2',
                bairro='Bairro 2',
                cidade='Cidade 2',
                estado='Estado 2',
                cep='22222222'
            )
        ]