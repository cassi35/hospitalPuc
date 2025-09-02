from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from src.domain.models.medicamento_model import Medicamento as MedicamentoDomain
from src.infra.db.entities.medicamento import Medicamento as MedicamentoEntity

class MedicamentoRepository(MedicamentoRepositoryInterface):
    
    def create(self, nome: str, descricao: str, fabricante: str, validade: str, quantidade_estoque: int) -> None:
        pass
    
    def update(self, id: int, nome: str, descricao: str, fabricante: str, validade: str, quantidade_estoque: int) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> MedicamentoDomain:
        pass
    
    def findAll(self) -> List[MedicamentoDomain]:
        pass
    
    def findByNome(self, nome: str) -> MedicamentoDomain:
        pass
