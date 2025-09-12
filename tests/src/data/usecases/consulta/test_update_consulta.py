from typing import Dict
from src.domain.usecases.consulta.update_consulta import ConsultaUpdateUseCase as ConsultaUpdateInterface
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface 
from src.infra.db.entities.consulta import Consulta

class ConsultaUpdateUseCase(ConsultaUpdateInterface):
    def __init__(self, consulta_repository: ConsultaRepositoryInterface):
        self.consulta_repository = consulta_repository
    
    def update(self, consulta_id: int, consulta: Consulta) -> Dict:
        pass
