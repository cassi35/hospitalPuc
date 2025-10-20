from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR,Text,Date,Enum,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.entities.setor import Setor
class Funcionario(Base):
    __tablename__ = 'funcionario'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    nome = Column(Text,nullable=False)
    cpf = Column(CHAR(11),nullable=False,unique=True)
    cargo = Column(Enum('enfermeiro','técnico','recepcionista'),nullable=False)
    setor_id = Column(Integer,ForeignKey('setor.id'),nullable=True)
    telefone = Column(CHAR(9),nullable=False)
    email = Column(String(255),nullable=False,unique=True)
    data_contratacao = Column(Date,nullable=False)
    usuario_id = Column(Integer,ForeignKey('Auth_user.id'),nullable=True)
    