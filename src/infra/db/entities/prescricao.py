from src.infra.db.settings.base import Base
from sqlalchemy import Column,Integer,Date,ForeignKey
from sqlalchemy.orm import relationship
class Prescricao(Base):
    __tablename__ = 'prescricao'
    id = Column(Integer,primary_key=True,autoincrement=True)
    paciente_id = Column(Integer,ForeignKey('Paciente.id'),nullable=True)
    medico_id = Column(Integer,ForeignKey('Medico.id'),nullable=True)
    data_prescricao = Column(Date,nullable=True)
    medicamento_id = Column(Integer,ForeignKey('medicamento.id'),nullable=True)
    dosagem = Column(Integer,nullable=True)
    frequencia = Column(Integer,nullable=True)
    
    paciente = relationship('Paciente')
    medico = relationship('Medico')
    medicamento = relationship('Medicamento')
