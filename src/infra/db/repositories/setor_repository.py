from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
from src.domain.models.setor_model import Setor as SetorDomain
from src.infra.db.entities.setor import Setor as SetorEntity

class SetorRepository(SetorRepositoryInterface):
    
    def create(self, nome: str, andar: int, capacidade: int, responsavel: str) -> None:
        with BDConnectionHandler() as database:
            try:
                setor = SetorEntity(
                    nome=nome,
                    andar=andar,
                    capacidade=capacidade,
                    responsavel=responsavel
                )
                database.session.add(setor)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def update(self, id: int, nome: str, andar: int, capacidade: int, responsavel: str) -> None:
        with BDConnectionHandler() as database:
            try:
                setor = database.session.query(SetorEntity).filter_by(id=id).first()
                if setor:
                    setor.nome = nome
                    setor.andar = andar
                    setor.capacidade = capacidade
                    setor.responsavel = responsavel
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                setor = database.session.query(SetorEntity).filter_by(id=id).first()
                if setor:
                    database.session.delete(setor)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> SetorDomain:
        with BDConnectionHandler() as database:
            try:
                setor = database.session.query(SetorEntity).filter_by(id=id).first()
                if setor:
                    return SetorDomain(
                        id=setor.id,
                        nome=setor.nome,
                        andar=setor.andar,
                        capacidade=setor.capacidade,
                        responsavel=setor.responsavel
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findAll(self) -> List[SetorDomain]:
        with BDConnectionHandler() as database:
            try:
                setores = database.session.query(SetorEntity).all()
                return [
                    SetorDomain(
                        id=setor.id,
                        nome=setor.nome,
                        andar=setor.andar,
                        capacidade=setor.capacidade,
                        responsavel=setor.responsavel
                    ) for setor in setores
                ]
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findByNome(self, nome: str) -> SetorDomain:
        with BDConnectionHandler() as database:
            try:
                setor = database.session.query(SetorEntity).filter_by(nome=nome).first()
                if setor:
                    return SetorDomain(
                        id=setor.id,
                        nome=setor.nome,
                        andar=setor.andar,
                        capacidade=setor.capacidade,
                        responsavel=setor.responsavel
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
