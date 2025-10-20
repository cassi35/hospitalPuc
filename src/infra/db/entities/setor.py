from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer
class Setor(Base):
    __tablename__ = 'setor'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    nome = Column(String(100),nullable=False)
    andar = Column(Integer,nullable=False)
    capacidade = Column(Integer,nullable=False)
    responsavel = Column(String(100),nullable=False)
