from src.infra.db.settings.base import Base
from sqlalchemy import Column,Integer,Date,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.entities.paciente import Paciente
from src.infra.db.entities.medico import Medico
from src.infra.db.entities.medicamento import Medicamento
class Prescricao(Base):
    __tablename__ = 'prescricao'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    paciente_id = Column(Integer,ForeignKey('Paciente.id'),nullable=True)
    medico_id = Column(Integer,ForeignKey('Medico.id'),nullable=True)
    data_prescricao = Column(Date,nullable=False)
    medicamento_id = Column(Integer,ForeignKey('medicamento.id'),nullable=False)
    dosagem = Column(Integer,nullable=False)
    frequencia = Column(Integer,nullable=False)
    
