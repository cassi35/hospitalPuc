from src.infra.db.settings.base import Base
from sqlalchemy import Column,Integer,Date,String,Enum,ForeignKey
from sqlalchemy.orm import relationship
class Consulta(Base):
    __tablename__ = 'Consulta'
    id = Column(Integer,primary_key=True,autoincrement=True)
    data_hora = Column(Date,nullable=True)
    paciente_id = Column(Integer,ForeignKey('Paciente.id'),nullable=True)
    medico_id = Column(Integer,ForeignKey('Medico.id'),nullable=True)
    especialidade_id = Column(Integer,ForeignKey('especialidade.id'),nullable=True)
    status = Column(Enum('ativo','nao ativo'),nullable=True)
    observacoes = Column(String(100),nullable=True)
    
    paciente = relationship('Paciente')
    medico = relationship('Medico')
    especialidade = relationship('Especialidade')
