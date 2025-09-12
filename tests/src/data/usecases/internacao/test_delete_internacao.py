from src.domain.usecases.internacao.delete_internacao import InternacaoDeleteUseCase as InternacaoDeleteInterface
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface

class InternacaoDeleteUseCase(InternacaoDeleteInterface):
    def __init__(self, internacao_repository: InternacaoRepositoryInterface):
        self.internacao_repository = internacao_repository
    
    def delete(self, internacao_id: int) -> None:
        pass
