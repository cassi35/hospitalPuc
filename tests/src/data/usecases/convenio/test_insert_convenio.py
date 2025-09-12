from typing import Dict
from src.domain.usecases.convenio.insert_convenio import ConvenioInsertUseCase as ConvenioInsertInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface 
from src.infra.db.entities.convenio import Convenio

class ConvenioInsertUseCase(ConvenioInsertInterface):
    def __init__(self, convenio_repository: ConvenioRepositoryInterface):
        self.convenio_repository = convenio_repository
    
    def insert(self, convenio: Convenio) -> Dict:
        pass
