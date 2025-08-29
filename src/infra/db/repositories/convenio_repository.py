from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface
from src.domain.models.convenio_model import Convenio as ConvenioDomain
from src.infra.db.entities.convenio import Convenio as ConvenioEntity
class ConvenioRepository(ConvenioRepositoryInterface):
    @classmethod
    def insert_convenio(cls,nome:str,tipo_plano:str)->None:
        with BDConnectionHandler() as database:
            try:
                convenio = ConvenioEntity(
                    nome=nome,
                    tipo_plano= tipo_plano
                )
                database.session.add(convenio)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    def delete_convenio(cls,id:int)->bool:
        with BDConnectionHandler() as database:
            try:
                convenio = database.session.query(ConvenioEntity).filter_by(id=id).first()
                if convenio:
                    database.session.delete(convenio)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e 
    def select_convenio(cls,id:int)->ConvenioDomain: 
        with BDConnectionHandler() as database:
            try:
                convenio = database.session.query(ConvenioEntity).filter_by(id=id).first()
                if convenio:
                    return ConvenioDomain(
                        id=id,
                        nome= convenio.nome,
                        tipo_plano=convenio.tipo_plano
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e 
    def udpate_convenio(cls,id:int,nome:str,tipo_plano:str)->None :
        with BDConnectionHandler() as database:
            try:
                convenio = database.session.query(ConvenioEntity).filter_by(id=id).first()
                if convenio:
                    convenio.nome = nome
                    convenio.tipo_plano = tipo_plano
                    database.session.commit()
                return None
            except Exception as e:
                database.session.rollback()
                raise e 