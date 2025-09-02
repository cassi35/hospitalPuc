from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface
from src.domain.models.leito_model import Leito as LeitoDomain
from src.infra.db.entities.leito import Leito as LeitoEntity

class LeitoRepository(LeitoRepositoryInterface):
    
    def create(self, numero_leito: str, setor_id: int, tipo: str, status: str) -> None:
        pass
    
    def update(self, id: int, numero_leito: str, setor_id: int, tipo: str, status: str) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> LeitoDomain:
        pass
    
    def findAll(self) -> List[LeitoDomain]:
        pass
    
    def findByStatus(self, status: str) -> List[LeitoDomain]:
        pass
