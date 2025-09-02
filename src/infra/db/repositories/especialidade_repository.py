from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface
from src.domain.models.especialidade_model import Especialidade as EspecialidadeDomain
from src.infra.db.entities.especialidade import Especialidade as EspecialidadeEntity
class EspecialidadeRepository(EspecialidadeRepositoryInterface):
    
    @classmethod
    def create(self, nome: str, descricao: str) -> None:
        with BDConnectionHandler() as database:
            try:
                especialidade = EspecialidadeEntity(
                    nome=nome,
                    descricao=descricao
                )
                database.session.add(especialidade)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def update(self, id: int, nome: str, descricao: str) -> None:
        with BDConnectionHandler() as database:
            try:
                especidade = database.session.query(EspecialidadeEntity).filter_by(id=id).first()
                if especidade:
                    especidade.nome = nome
                    especidade.descricao = descricao
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                especialidade = database.session.query(EspecialidadeEntity).filter_by(id=id).first()
                if especialidade:
                    database.session.delete(especialidade)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> EspecialidadeDomain:
        with BDConnectionHandler() as database:
            try:
                especialidade = database.session.query(EspecialidadeEntity).filter_by(id=id).first()
                if especialidade:
                    return EspecialidadeDomain(
                        id=especialidade.id,
                        nome=especialidade.nome,
                        descricao=especialidade.descricao
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e 

    def findAll(self) -> List[EspecialidadeDomain]:
        with BDConnectionHandler() as database:
            try:
                especialidades = database.session.query(EspecialidadeEntity).all()
                return [
                    EspecialidadeDomain(
                        id=especidade.id,
                        nome=especidade.nome,
                        descricao=especidade.descricao
                    ) for especidade in especialidades
                ]
            except Exception as e:
                database.session.rollback()
                raise e
