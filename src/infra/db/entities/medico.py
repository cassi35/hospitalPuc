from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR,Enum,Text,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.entities.especialidade import Especialidade
class Medico(Base):
    __tablename__ = 'Medico'
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(20),nullable=True)
    cpf = Column(CHAR(11),nullable=True)
    especialidade_id = Column(Integer,ForeignKey('especialidade.id'),nullable=True)
    telefone = Column(CHAR(9),nullable=True)
    email = Column(Text,nullable=True)
    status = Column(Enum('ativo','nao ativo'),nullable=True)
    
    especialidade = relationship(Especialidade)
    usuario_id = Column(Integer,ForeignKey('Auth_user.id'),nullable=True)