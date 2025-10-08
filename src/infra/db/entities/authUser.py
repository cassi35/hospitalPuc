from src.infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP

class AuthUser(Base):
    __tablename__ = 'Auth_user' 
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    nome = Column(String(30), nullable=False)
    senha = Column(String(255),nullable=False)
    role = Column(Enum('Paciente', 'Medico', 'funcionario'),nullable=False)
    createdAt = Column(TIMESTAMP,nullable=False,server_default='CURRENT_TIMESTAMP')
    updatedAt = Column(TIMESTAMP,nullable=False,server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
