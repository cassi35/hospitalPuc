from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface
from src.domain.models.internacao_model import Internacao as InternacaoDomain
from src.infra.db.entities.internacao import Internacao as InternacaoEntity

class InternacaoRepository(InternacaoRepositoryInterface):
    
    def create(self, paciente_id: int, medico_id: int, leito_id: int, data_entrada: str, status: str) -> None:
        pass
    
    def update(self, id: int, paciente_id: int, medico_id: int, leito_id: int, data_entrada: str, status: str) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> InternacaoDomain:
        pass
    
    def findAll(self) -> List[InternacaoDomain]:
        pass
    
    def findByPaciente(self, paciente_id: int) -> List[InternacaoDomain]:
        pass
