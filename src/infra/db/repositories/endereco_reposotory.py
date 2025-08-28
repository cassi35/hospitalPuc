from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface
from src.domain.models.endereco_model import Endereco as EnderecoDomain
from src.infra.db.entities.endereco import Endereco as EnderecoEntity
from sqlalchemy import select
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
    
    def select_endereco(cls, id: int) -> EnderecoDomain:
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
    def update_endereco(cls, id: int, rua: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        with BDConnectionHandler() as database:
            try:
                endereco = database.session.query(EnderecoEntity).filter_by(id=id).first()
                if endereco:
                    endereco.bairro = bairro
                    endereco.cep = cep
                    endereco.cidade = cidade
                    endereco.rua = rua
                    endereco.estado = estado
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e 
    def delete_endereco(cls, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                endereco = database.session.query(EnderecoEntity).filter_by(id=id).first()
                if endereco:
                    database.session.delete(endereco)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    def find_by_cep(cls, cep: str) -> List[EnderecoDomain]:
        with BDConnectionHandler() as database:
            try:
                stmt = select(EnderecoEntity).where(EnderecoEntity.cep == cep)
                result = database.session.execute(stmt)
                enderecos = result.scalars().all()
                return [
                    EnderecoDomain(
                        id=e.id,
                        rua=e.rua,
                        bairro=e.bairro,
                        cidade=e.cidade,
                        estado=e.estado,
                        cep=e.cep
                    )
                    for e in enderecos
                ]
            except Exception as e:
                database.session.rollback()
                raise e
    def select_all_enderecos(self) -> List[EnderecoDomain]:pass