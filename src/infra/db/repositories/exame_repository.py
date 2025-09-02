from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface
from src.domain.models.exame_model import Exame as ExameDomain
from src.infra.db.entities.exame import Exame as ExameEntity

class ExameRepository(ExameRepositoryInterface):
    
    def create(self, tipo_exame: str, data_exame: str, paciente_id: int, medico_id: int, resultado: str, status: str) -> None:
        pass
    
    def update(self, id: int, tipo_exame: str, data_exame: str, paciente_id: int, medico_id: int, resultado: str, status: str) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> ExameDomain:
        pass
    
    def findAll(self) -> List[ExameDomain]:
        pass
