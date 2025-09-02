from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface
from src.domain.models.especialidade_model import Especialidade as EspecialidadeDomain
from src.infra.db.entities.especialidade import Especialidade as EspecialidadeEntity
class EspecialidadeRepository(EspecialidadeRepositoryInterface):
    
    @classmethod
    def create(self, nome: str, descricao: str) -> None:
        pass
    
    def update(self, id: int, nome: str, descricao: str) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> EspecialidadeDomain:
        pass
    
    def findAll(self) -> List[EspecialidadeDomain]:
        pass
