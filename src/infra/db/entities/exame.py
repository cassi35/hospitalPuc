from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,Date,Text,Enum,ForeignKey
from sqlalchemy.orm import relationship
class Exame(Base):
    __tablename__ = 'Exame'
    id = Column(Integer,primary_key=True,autoincrement=True)
    tipo_exame = Column(Text,nullable=True)
    data_exame = Column(Date,nullable=True)
    paciente_id = Column(Integer,ForeignKey('Paciente.id'),nullable=True)
    medico_id = Column(Integer,ForeignKey('Medico.id'),nullable=True)
    resultado = Column(Text,nullable=True)
    status = Column(Enum('solicitado','em andamento','concluído'),nullable=True)
    
    paciente = relationship('Paciente')
    medico = relationship('Medico')
