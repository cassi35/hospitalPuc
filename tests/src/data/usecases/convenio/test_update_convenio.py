from typing import Dict
from src.domain.usecases.convenio.update_convenio import ConvenioUpdateUseCase as ConvenioUpdateInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface 
from src.infra.db.entities.convenio import Convenio

class ConvenioUpdateUseCase(ConvenioUpdateInterface):
    def __init__(self, convenio_repository: ConvenioRepositoryInterface):
        self.convenio_repository = convenio_repository
    
    def update(self, convenio_id: int, convenio: Convenio) -> Dict:
        pass
