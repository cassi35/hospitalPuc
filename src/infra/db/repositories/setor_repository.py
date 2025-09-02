from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
from src.domain.models.setor_model import Setor as SetorDomain
from src.infra.db.entities.setor import Setor as SetorEntity

class SetorRepository(SetorRepositoryInterface):
    
    def create(self, nome: str, andar: int, capacidade: int, responsavel: str) -> None:
        pass
    
    def update(self, id: int, nome: str, andar: int, capacidade: int, responsavel: str) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> SetorDomain:
        pass
    
    def findAll(self) -> List[SetorDomain]:
        pass
    
    def findByNome(self, nome: str) -> SetorDomain:
        pass
