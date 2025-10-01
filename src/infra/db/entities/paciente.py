from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR,Date,Enum,Text,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.entities.endereco import Endereco
from src.infra.db.entities.convenio import Convenio
class Paciente(Base):
    __tablename__ = 'Paciente'
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(20),nullable=True)
    cpf = Column(CHAR(11),nullable=True)
    data_nascimento = Column(Date,nullable=True)
    sexo = Column(Enum('m','f'),nullable=True)
    telefone = Column(CHAR(11),nullable=True)
    alergia = Column(Text,nullable=True)
    contato_emergencia = Column(CHAR(11),nullable=True)
    email = Column(String(30),nullable=True)
    endereco_id = Column(Integer,ForeignKey('Endereco.id'),nullable=True)
    convenio_id = Column(Integer,ForeignKey('convenio.id'),nullable=True)
    endereco = relationship(Endereco)
    convenio = relationship(Convenio)
