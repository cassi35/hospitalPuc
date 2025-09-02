from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface
from src.domain.models.consulta_model import Consulta as ConsultaDomain
from src.infra.db.entities.consulta import Consulta as ConsultaEntity

class ConsultaRepository(ConsultaRepositoryInterface):
    
    def create(self, data_hora: str, paciente_id: int, medico_id: int, especialidade_id: int, status: str, observacoes: str) -> None:
        pass
    
    def update(self, id: int, data_hora: str, paciente_id: int, medico_id: int, especialidade_id: int, status: str, observacoes: str) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> ConsultaDomain:
        pass
    
    def findAll(self) -> List[ConsultaDomain]:
        pass
    

