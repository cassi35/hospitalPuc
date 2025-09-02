from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface
from src.domain.models.consulta_model import Consulta as ConsultaDomain
from src.infra.db.entities.consulta import Consulta as ConsultaEntity

class ConsultaRepository(ConsultaRepositoryInterface):
    
    def create(self, data_hora: str, paciente_id: int, medico_id: int, especialidade_id: int, status: str, observacoes: str) -> None:
        with BDConnectionHandler() as database:
            try:
                consulta = ConsultaEntity(
                    data_hora=data_hora,
                    paciente_id=paciente_id,
                    medico_id=medico_id,
                    especialidade_id=especialidade_id,
                    status=status,
                    observacoes=observacoes
                )
                database.session.add(consulta)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def update(self, id: int, data_hora: str, paciente_id: int, medico_id: int, especialidade_id: int, status: str, observacoes: str) -> None:
        with BDConnectionHandler() as database:
            try:
                consulta = database.session.query(ConsultaEntity).filter_by(id=id).first()
                if consulta:
                    consulta.data_hora = data_hora
                    consulta.paciente_id = paciente_id
                    consulta.medico_id = medico_id
                    consulta.especialidade_id = especialidade_id
                    consulta.status = status
                    consulta.observacoes = observacoes
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                consulta = database.session.query(ConsultaEntity).filter_by(id=id).first()
                if consulta:
                    database.session.delete(consulta)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> ConsultaDomain:
        with BDConnectionHandler() as database:
            try:
                consulta = database.session.query(ConsultaEntity).filter_by(id=id).first()
                if consulta:
                    return ConsultaDomain(
                        id=consulta.id,
                        data_hora=consulta.data_hora,
                        paciente_id=consulta.paciente_id,
                        medico_id=consulta.medico_id,
                        especialidade_id=consulta.especialidade_id,
                        status=consulta.status,
                        observacoes=consulta.observacoes
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findAll(self) -> List[ConsultaDomain]:
        with BDConnectionHandler() as database:
            try:
                consultas = database.session.query(ConsultaEntity).all()
                return [
                    ConsultaDomain(
                        id=consulta.id,
                        data_hora=consulta.data_hora,
                        paciente_id=consulta.paciente_id,
                        medico_id=consulta.medico_id,
                        especialidade_id=consulta.especialidade_id,
                        status=consulta.status,
                        observacoes=consulta.observacoes
                    ) for consulta in consultas
                ]
            except Exception as e:
                database.session.rollback()
                raise e
    
