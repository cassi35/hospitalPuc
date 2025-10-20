from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR,Enum,Text,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.entities.especialidade import Especialidade
class Medico(Base):
    __tablename__ = 'Medico'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    nome = Column(String(20),nullable=False)
    cpf = Column(CHAR(11),nullable=False)
    especialidade_id = Column(Integer,ForeignKey('especialidade.id'),nullable=False)
    telefone = Column(CHAR(9),nullable=False,unique=True)
    email = Column(String(255),nullable=False,unique=True)
    status = Column(Enum('ativo','nao ativo'),nullable=False)
    usuario_id = Column(Integer,ForeignKey('Auth_user.id'),nullable=True)