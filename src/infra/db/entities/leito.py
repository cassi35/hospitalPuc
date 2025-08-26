from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,Enum,ForeignKey
from sqlalchemy.orm import relationship
class Leito(Base):
    __tablename__ = 'leito'
    id = Column(Integer,primary_key=True,autoincrement=True)
    numero_leito = Column(String(30),nullable=True)
    setor_id = Column(Integer,ForeignKey('setor.id'),nullable=True)
    tipo = Column(Enum('Enfermaria','Apartamento','UTI Adulto','UTI Neonatal','UTI Pediátrica'),nullable=True)
    status = Column(Enum('disponivel','ocupado'),nullable=True)
    
    setor = relationship('Setor')
