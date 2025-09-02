from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface
from src.domain.models.internacao_model import Internacao as InternacaoDomain
from src.infra.db.entities.internacao import Internacao as InternacaoEntity

class InternacaoRepository(InternacaoRepositoryInterface):
    
    def create(self, paciente_id: int, medico_id: int, leito_id: int, data_entrada: str, status: str) -> None:
        with BDConnectionHandler() as database:
            try:
                internacao = InternacaoEntity(
                    paciente_id=paciente_id,
                    medico_id=medico_id,
                    leito_id=leito_id,
                    data_entrada=data_entrada,
                    status=status
                )
                database.session.add(internacao)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def update(self, id: int, paciente_id: int, medico_id: int, leito_id: int, data_entrada: str, status: str) -> None:
        with BDConnectionHandler() as database:
            try:
                internacao = database.session.query(InternacaoEntity).filter_by(id=id).first()
                if internacao:
                    internacao.paciente_id = paciente_id
                    internacao.medico_id = medico_id
                    internacao.leito_id = leito_id
                    internacao.data_entrada = data_entrada
                    internacao.status = status
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                internacao = database.session.query(InternacaoEntity).filter_by(id=id).first()
                if internacao:
                    database.session.delete(internacao)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> InternacaoDomain:
        with BDConnectionHandler() as database:
            try:
                internacao = database.session.query(InternacaoEntity).filter_by(id=id).first()
                if internacao:
                    return InternacaoDomain(
                        id=internacao.id,
                        paciente_id=internacao.paciente_id,
                        medico_id=internacao.medico_id,
                        leito_id=internacao.leito_id,
                        data_entrada=internacao.data_entrada,
                        status=internacao.status
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findAll(self) -> List[InternacaoDomain]:
        with BDConnectionHandler() as database:
            try:
                internacoes = database.session.query(InternacaoEntity).all()
                return [
                    InternacaoDomain(
                        id=internacao.id,
                        paciente_id=internacao.paciente_id,
                        medico_id=internacao.medico_id,
                        leito_id=internacao.leito_id,
                        data_entrada=internacao.data_entrada,
                        status=internacao.status
                    ) for internacao in internacoes
                ]
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findByPaciente(self, paciente_id: int) -> List[InternacaoDomain]:
        with BDConnectionHandler() as database:
            try:
                internacoes = database.session.query(InternacaoEntity).filter_by(paciente_id=paciente_id).all()
                return [
                    InternacaoDomain(
                        id=internacao.id,
                        paciente_id=internacao.paciente_id,
                        medico_id=internacao.medico_id,
                        leito_id=internacao.leito_id,
                        data_entrada=internacao.data_entrada,
                        status=internacao.status
                    ) for internacao in internacoes
                ]
            except Exception as e:
                database.session.rollback()
                raise e
