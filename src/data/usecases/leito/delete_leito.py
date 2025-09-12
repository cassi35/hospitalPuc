from src.domain.usecases.leito.delete_leito import LeitoDeleteUseCase as LeitoDeleteInterface
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface

class LeitoDeleteUseCase(LeitoDeleteInterface):
    def __init__(self, leito_repository: LeitoRepositoryInterface):
        self.leito_repository = leito_repository
    
    def delete(self, leito_id: int) -> None:
        pass
