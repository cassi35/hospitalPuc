from src.domain.usecases.convenio.delete_convenio import ConvenioDeleteUseCase as ConvenioDeleteInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface

class ConvenioDeleteUseCase(ConvenioDeleteInterface):
    def __init__(self, convenio_repository: ConvenioRepositoryInterface):
        self.convenio_repository = convenio_repository
    
    def delete(self, convenio_id: int) -> None:
        pass
