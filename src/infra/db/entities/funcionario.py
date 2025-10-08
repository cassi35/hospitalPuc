from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR,Text,Date,Enum,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.entities.setor import Setor
class Funcionario(Base):
    __tablename__ = 'funcionario'
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(Text,nullable=True)
    cpf = Column(CHAR(11),nullable=True)
    cargo = Column(Enum('enfermeiro','técnico','recepcionista'),nullable=True)
    setor_id = Column(Integer,ForeignKey('setor.id'),nullable=True)
    telefone = Column(CHAR(9),nullable=True)
    email = Column(Text,nullable=True)
    data_contratacao = Column(Date,nullable=True)
    usuario_id = Column(Integer,ForeignKey('Auth_user.id'),nullable=True)
    setor = relationship(Setor)
