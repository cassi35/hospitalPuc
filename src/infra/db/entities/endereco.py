from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR
class Endereco(Base):
    __tablename__ = 'Endereco'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    rua = Column(String(30),nullable=False)
    bairro = Column(String(30),nullable=False)
    cidade = Column(String(30),nullable=False)
    estado = Column(String(30),nullable=False)
    cep = Column(CHAR(8),nullable=False)