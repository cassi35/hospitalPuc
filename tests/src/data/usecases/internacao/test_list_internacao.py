from typing import List, Dict
from src.domain.usecases.internacao.list_internacao import InternacaoListUseCase as InternacaoListInterface
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface

class InternacaoListUseCase(InternacaoListInterface):
    def __init__(self, internacao_repository: InternacaoRepositoryInterface):
        self.internacao_repository = internacao_repository
    
    def list(self) -> List[Dict]:
        pass
