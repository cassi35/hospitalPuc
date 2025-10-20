from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,CHAR,Enum
class Convenio(Base):
    __tablename__ = 'convenio'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False  )
    nome = Column(String(30),nullable=False)
    tipo_plano = Column(Enum('Individual','Familiar','Empresarial'),nullable=False)