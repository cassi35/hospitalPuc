from src.infra.db.settings.base import Base
from sqlalchemy import Column,String,Integer,Date,Float,Enum,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.entities.paciente import Paciente
from src.infra.db.entities.convenio import Convenio
class Financeiro(Base):
    __tablename__ = 'financeiro'
    id = Column(Integer,primary_key=True,autoincrement=True)
    paciente_id = Column(Integer,ForeignKey('Paciente.id'),nullable=True)
    convenio_id = Column(Integer,ForeignKey('convenio.id'),nullable=True)
    valor = Column(Float,nullable=True)
    data_emissao = Column(Date,nullable=True)
    data_vencimento = Column(Date,nullable=True)
    status_pagamento = Column(Enum('pago','pendente','cancelado'),nullable=True)
    
    paciente = relationship(Paciente)
    convenio = relationship(Convenio)
