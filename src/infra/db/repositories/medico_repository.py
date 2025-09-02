from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.domain.models.medico_model import Medico as MedicoDomain
from src.infra.db.entities.medico import Medico as MedicoEntity

class MedicoRepository(MedicoRepositoryInterface):
    
    def create(self, nome: str, cpf: str, especialidade_id: int, telefone: str, email: str, status: str) -> None:
        pass
    
    def update(self, id: int, nome: str, cpf: str, especialidade_id: int, telefone: str, email: str, status: str) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> MedicoDomain:
        pass
    
    def findAll(self) -> List[MedicoDomain]:
        pass
    
    def findByCpf(self, cpf: str) -> MedicoDomain:
        pass
