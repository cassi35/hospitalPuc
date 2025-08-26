from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR,Enum,Text,ForeignKey
from sqlalchemy.orm import relationship
class Medico(Base):
    __tablename__ = 'Medico'
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(20),nullable=True)
    cpf = Column(CHAR(11),nullable=True)
    especialidade_id = Column(Integer,ForeignKey('especialidade.id'),nullable=True)
    telefone = Column(CHAR(9),nullable=True)
    email = Column(Text,nullable=True)
    status = Column(Enum('ativo','nao ativo'),nullable=True)
    
    especialidade = relationship('Especialidade')
