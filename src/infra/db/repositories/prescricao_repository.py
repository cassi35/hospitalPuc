from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface
from src.domain.models.prescricao_model import Prescricao as PrescricaoDomain
from src.infra.db.entities.prescricao import Prescricao as PrescricaoEntity

class PrescricaoRepository(PrescricaoRepositoryInterface):
    
    def create(self, paciente_id: int, medico_id: int, data_prescricao: str, medicamento_id: int, dosagem: int, frequencia: int) -> None:
        pass
    
    def update(self, id: int, paciente_id: int, medico_id: int, data_prescricao: str, medicamento_id: int, dosagem: int, frequencia: int) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> PrescricaoDomain:
        pass
    
    def findAll(self) -> List[PrescricaoDomain]:
        pass
    
    def findByPaciente(self, paciente_id: int) -> List[PrescricaoDomain]:
        pass
    
    def findByMedico(self, medico_id: int) -> List[PrescricaoDomain]:
        pass
