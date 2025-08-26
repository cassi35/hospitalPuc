from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR
class Endereco(Base):
    __tablename__ = 'Endereco'
    id = Column(Integer,primary_key=True,autoincrement=True)
    rua = Column(String(30),nullable=True)
    bairro = Column(String(30),nullable=True)
    cidade = Column(String(30),nullable=True)
    estado = Column(String(30),nullable=True)
    cep = Column(CHAR(8),nullable=True)