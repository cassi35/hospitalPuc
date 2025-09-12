from src.domain.usecases.setor.delete_setor import SetorDeleteUseCase as SetorDeleteInterface
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface

class SetorDeleteUseCase(SetorDeleteInterface):
    def __init__(self, setor_repository: SetorRepositoryInterface):
        self.setor_repository = setor_repository
    
    def delete(self, setor_id: int) -> None:
        pass
