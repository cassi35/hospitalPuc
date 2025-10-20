from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR,Date,Enum,Text,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.entities.endereco import Endereco
from src.infra.db.entities.convenio import Convenio
class Paciente(Base):
    __tablename__ = 'Paciente'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    nome = Column(String(20),nullable=False)
    cpf = Column(CHAR(11),nullable=False)
    data_nascimento = Column(Date,nullable=False)
    sexo = Column(Enum('m','f'),nullable=False)
    telefone = Column(CHAR(11),nullable=False)
    alergia = Column(Text)
    contato_emergencia = Column(CHAR(11),nullable=False)
    email = Column(String(255),nullable=False)
    endereco_id = Column(Integer,ForeignKey('Endereco.id'),nullable=True)
    convenio_id = Column(Integer,ForeignKey('convenio.id'),nullable=True)
    usuario_id = Column(Integer,ForeignKey('Auth_user.id'),nullable=True)