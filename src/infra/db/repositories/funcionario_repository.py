from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface
from src.domain.models.funcionario_model import Funcionario as FuncionarioDomain
from src.infra.db.entities.funcionario import Funcionario as FuncionarioEntity

class FuncionarioRepository(FuncionarioRepositoryInterface):
    
    def create(self, nome: str, cpf: str, cargo: str, setor_id: int, telefone: str, email: str, data_contratacao: str) -> None:
        pass
    
    def update(self, id: int, nome: str, cpf: str, cargo: str, setor_id: int, telefone: str, email: str, data_contratacao: str) -> None:
        pass
    
    def delete(self, id: int) -> bool:
        pass
    
    def findById(self, id: int) -> FuncionarioDomain:
        pass
    
    def findAll(self) -> List[FuncionarioDomain]:
        pass
    
    def findByCpf(self, cpf: str) -> FuncionarioDomain:
        pass
    
    def findByCargo(self, cargo: str) -> List[FuncionarioDomain]:
        pass
