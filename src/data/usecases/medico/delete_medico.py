from src.domain.usecases.medico.delete_medico import MedicoDeleteUseCase as MedicoDeleteInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface

class MedicoDeleteUseCase(MedicoDeleteInterface):
    def __init__(self, medico_repository: MedicoRepositoryInterface):
        self.medico_repository = medico_repository
    
    def delete(self, medico_id: int) -> None:
        pass
