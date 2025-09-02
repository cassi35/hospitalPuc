from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface
from src.domain.models.leito_model import Leito as LeitoDomain
from src.infra.db.entities.leito import Leito as LeitoEntity

class LeitoRepository(LeitoRepositoryInterface):
    
    def create(self, numero_leito: str, setor_id: int, tipo: str, status: str) -> None:
        with BDConnectionHandler() as database:
            try:
                leito = LeitoEntity(
                   numero_leito= numero_leito,
                   setor_id=setor_id,
                   tipo=tipo,
                   status= status
                )
                database.session.add(leito)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e 
    def update(self, id: int, numero_leito: str, setor_id: int, tipo: str, status: str) -> None:
            with BDConnectionHandler() as database:
                try:
                    leito = database.session.query(LeitoEntity).filter_by(id=id).first()
                    if leito:
                        leito.numero_leito = numero_leito
                        leito.setor_id = setor_id
                        leito.tipo = tipo
                        leito.status = status
                        database.session.commit()
                except Exception as e:
                    database.session.rollback()
                    raise e
    
    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                leito = database.session.query(LeitoEntity).filter_by(id=id).first()
                if leito:
                    database.session.delete(leito)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> LeitoDomain:
        with BDConnectionHandler() as database:
            try:
                leito = database.session.query(LeitoEntity).filter_by(id=id).first()
                if leito:
                    return LeitoDomain(
                   numero_leito= leito.numero_leito,
                   setor_id=leito.setor_id,
                   tipo=leito.tipo,
                   status= leito.status
                )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findAll(self) -> List[LeitoDomain]:
        with BDConnectionHandler() as database:
            try:
                leitos = database.session.query(LeitoEntity).all()
                return [
                  LeitoDomain(
                   numero_leito= leito.numero_leito,
                   setor_id=leito.setor_id,
                   tipo=leito.tipo,
                   status= leito.status
                ) for leito in leitos
                ]
            except Exception as e:
                database.session.rollback()
                raise e
    def findByStatus(self, status: str) -> List[LeitoDomain]:
        with BDConnectionHandler() as database:
            try:
                leitos = database.session.query(LeitoEntity).filter_by(status=status).all()
                return [
                  LeitoDomain(
                   numero_leito= leito.numero_leito,
                   setor_id=leito.setor_id,
                   tipo=leito.tipo,
                   status= leito.status
                ) for leito in leitos
                ]
            except Exception as e:
                database.session.rollback()
                raise e
