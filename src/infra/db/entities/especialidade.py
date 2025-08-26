from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,Text
class Especialidade(Base):
    __tablename__ = 'especialidade'
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(50),nullable=True)
    descricao = Column(Text, nullable=True)
