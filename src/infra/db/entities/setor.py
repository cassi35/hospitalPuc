from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer
class Setor(Base):
    __tablename__ = 'setor'
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(100),nullable=True)
    andar = Column(Integer,nullable=True)
    capacidade = Column(Integer,nullable=True)
    responsavel = Column(String(100),nullable=True)
