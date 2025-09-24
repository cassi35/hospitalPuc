from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface
from src.domain.models.exame_model import Exame as ExameDomain
from src.infra.db.entities.exame import Exame as ExameEntity

class ExameRepository(ExameRepositoryInterface):

    @classmethod
    def create(cls, tipo_exame: str, data_exame: str, paciente_id: int, medico_id: int, resultado: str, status: str) -> None:
        with BDConnectionHandler() as database:
            try:
                exame = ExameEntity(
                    tipo_exame=tipo_exame,
                    data_exame=data_exame,
                    paciente_id=paciente_id,
                    medico_id=medico_id,
                    resultado=resultado,
                    status=status
                )
                database.session.add(exame)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e

    @classmethod
    def update(cls, id: int, tipo_exame: str, data_exame: str, paciente_id: int, medico_id: int, resultado: str, status: str) -> None:
        with BDConnectionHandler() as database:
            try:
                exame = database.session.query(ExameEntity).filter_by(id=id).first()
                if exame:
                    exame.tipo_exame = tipo_exame
                    exame.data_exame = data_exame
                    exame.paciente_id = paciente_id
                    exame.medico_id = medico_id
                    exame.resultado = resultado
                    exame.status = status
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e

    @classmethod
    def delete(cls, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                exame = database.session.query(ExameEntity).filter_by(id=id).first()
                if exame:
                    database.session.delete(exame)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e

    @classmethod
    def findById(cls, id: int) -> ExameDomain:
        with BDConnectionHandler() as database:
            try:
                exame = database.session.query(ExameEntity).filter_by(id=id).first()
                if exame:
                    return ExameDomain(
                        id=exame.id,
                        tipo_exame=exame.tipo_exame,
                        data_exame=exame.data_exame,
                        paciente_id=exame.paciente_id,
                        medico_id=exame.medico_id,
                        resultado=exame.resultado,
                        status=exame.status
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e

    @classmethod
    def findAll(cls) -> List[ExameDomain]:
        with BDConnectionHandler() as database:
            try:
                exames = database.session.query(ExameEntity).all()
                return [
                    ExameDomain(
                        id=exame.id,
                        tipo_exame=exame.tipo_exame,
                        data_exame=exame.data_exame,
                        paciente_id=exame.paciente_id,
                        medico_id=exame.medico_id,
                        resultado=exame.resultado,
                        status=exame.status
                    ) for exame in exames
                ]
            except Exception as e:
                database.session.rollback()
                raise e
