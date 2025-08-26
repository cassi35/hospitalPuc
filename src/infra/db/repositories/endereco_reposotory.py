from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface
from src.domain.models.endereco_model import Endereco as EnderecoDomain
from src.infra.db.entities.endereco import Endereco as EnderecoEntity
class EnderecoRepository(EnderecoRepositoryInterface):
    @classmethod
    def insert_endereco(cls, rua: str, bairro: str, cidade: str, estado: str, cep: str)-> None:
        with BDConnectionHandler() as database:
            try:
                endereco = EnderecoEntity(
                    rua=rua,
                    bairro=bairro,
                    cidade=cidade,
                    estado=estado,
                    cep=cep
                )
                database.session.add(endereco)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e 
    
    def select_endereco(self, id: int) -> EnderecoDomain:
        with BDConnectionHandler() as database:
            try:
               endereco = database.session. query(EnderecoEntity).filter_by(id=id).first()
               if endereco:
                    return EnderecoDomain(
                        id=endereco.id,
                        rua=endereco.rua,
                        bairro=endereco.bairro,
                        cidade=endereco.cidade,
                        estado=endereco.estado,
                        cep=endereco.cep
                    )
               return None
            except Exception as e:
                database.session.rollback()
                raise e 
    def delete_endereco(self, id: int) -> None:
        pass
    def select_all_enderecos(self) -> List[EnderecoDomain]:pass
    def update_endereco(self, id: int, rua: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        pass
    def find_by_cep(self, cep: str) -> List[EnderecoDomain]:
        pass