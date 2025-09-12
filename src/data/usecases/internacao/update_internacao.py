from typing import Dict
from src.domain.usecases.internacao.update_internacao import InternacaoUpdateUseCase as InternacaoUpdateInterface
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface 
from src.infra.db.entities.internacao import Internacao

class InternacaoUpdateUseCase(InternacaoUpdateInterface):
    def __init__(self, internacao_repository: InternacaoRepositoryInterface):
        self.internacao_repository = internacao_repository
    
    def update(self, internacao_id: int, internacao: Internacao) -> Dict:
        pass
