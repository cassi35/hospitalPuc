from src.infra.db.settings.base import Base
from sqlalchemy import Column,Integer,Date,Enum,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.entities.paciente import Paciente
from src.infra.db.entities.medico import Medico
from src.infra.db.entities.leito import Leito
class Internacao(Base):
    __tablename__ = 'internacao'
    id = Column(Integer,primary_key=True,autoincrement=True)
    paciente_id = Column(Integer,ForeignKey('Paciente.id'),nullable=True)
    medico_id = Column(Integer,ForeignKey('Medico.id'),nullable=True)
    leito_id = Column(Integer,ForeignKey('leito.id'),nullable=True)
    data_entrada = Column(Date,nullable=True)
    status = Column(Enum('em andamento','alta','obito'),nullable=True)
    
    paciente = relationship(Paciente)
    medico = relationship(Medico)
    leito = relationship(Leito)
