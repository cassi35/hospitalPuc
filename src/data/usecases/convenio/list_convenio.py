from typing import List, Dict
from src.domain.usecases.convenio.list_convenio import ConvenioListUseCase as ConvenioListInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface

class ConvenioListUseCase(ConvenioListInterface):
    def __init__(self, convenio_repository: ConvenioRepositoryInterface):
        self.convenio_repository = convenio_repository
    
    def list(self) -> List[Dict]:
        pass
