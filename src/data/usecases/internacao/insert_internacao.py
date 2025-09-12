from typing import Dict
from src.domain.usecases.internacao.insert_internacao import InternacaoInsertUseCase as InternacaoInsertInterface
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface 
from src.infra.db.entities.internacao import Internacao

class InternacaoInsertUseCase(InternacaoInsertInterface):
    def __init__(self, internacao_repository: InternacaoRepositoryInterface):
        self.internacao_repository = internacao_repository
    
    def insert(self, internacao: Internacao) -> Dict:
        pass
