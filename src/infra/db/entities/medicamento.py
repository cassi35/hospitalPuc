from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,Text,Date
class Medicamento(Base):
    __tablename__ = 'medicamento'
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(30),nullable=True)
    descricao = Column(String(30),nullable=True)
    fabricante = Column(Text,nullable=True)
    validade = Column(Date,nullable=True)
    quantidade_estoque = Column(Integer,nullable=True)
