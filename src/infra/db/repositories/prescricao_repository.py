from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface
from src.domain.models.prescricao_model import Prescricao as PrescricaoDomain
from src.infra.db.entities.prescricao import Prescricao as PrescricaoEntity

class PrescricaoRepository(PrescricaoRepositoryInterface):
    
    def create(self, paciente_id: int, medico_id: int, data_prescricao: str, medicamento_id: int, dosagem: int, frequencia: int) -> None:
        with BDConnectionHandler() as database:
            try:
                prescricao = PrescricaoEntity(
                    paciente_id=paciente_id,
                    medico_id=medico_id,
                    data_prescricao=data_prescricao,
                    medicamento_id=medicamento_id,
                    dosagem=dosagem,
                    frequencia=frequencia
                )
                database.session.add(prescricao)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def update(self, id: int, paciente_id: int, medico_id: int, data_prescricao: str, medicamento_id: int, dosagem: int, frequencia: int) -> None:
        with BDConnectionHandler() as database:
            try:
                prescricao = database.session.query(PrescricaoEntity).filter_by(id=id).first()
                if prescricao:
                    prescricao.paciente_id = paciente_id
                    prescricao.medico_id = medico_id
                    prescricao.data_prescricao = data_prescricao
                    prescricao.medicamento_id = medicamento_id
                    prescricao.dosagem = dosagem
                    prescricao.frequencia = frequencia
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                prescricao = database.session.query(PrescricaoEntity).filter_by(id=id).first()
                if prescricao:
                    database.session.delete(prescricao)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> PrescricaoDomain:
        with BDConnectionHandler() as database:
            try:
                prescricao = database.session.query(PrescricaoEntity).filter_by(id=id).first()
                if prescricao:
                    return PrescricaoDomain(
                        id=prescricao.id,
                        paciente_id=prescricao.paciente_id,
                        medico_id=prescricao.medico_id,
                        data_prescricao=prescricao.data_prescricao,
                        medicamento_id=prescricao.medicamento_id,
                        dosagem=prescricao.dosagem,
                        frequencia=prescricao.frequencia
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findAll(self) -> List[PrescricaoDomain]:
        with BDConnectionHandler() as database:
            try:
                prescricoes = database.session.query(PrescricaoEntity).all()
                return [
                    PrescricaoDomain(
                        id=prescricao.id,
                        paciente_id=prescricao.paciente_id,
                        medico_id=prescricao.medico_id,
                        data_prescricao=prescricao.data_prescricao,
                        medicamento_id=prescricao.medicamento_id,
                        dosagem=prescricao.dosagem,
                        frequencia=prescricao.frequencia
                    ) for prescricao in prescricoes
                ]
            except Exception as e:
                database.session.rollback()
                raise e
