from typing import Dict
from src.domain.usecases.consulta.insert_consulta import ConsultaInsertUseCase as ConsultaInsertInterface
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface 
from src.infra.db.entities.consulta import Consulta

class ConsultaInsertUseCase(ConsultaInsertInterface):
    def __init__(self, consulta_repository: ConsultaRepositoryInterface):
        self.consulta_repository = consulta_repository
    
    def insert(self, consulta: Consulta) -> Dict:
        pass
