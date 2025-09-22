from typing import List, Dict

from src.domain.usecases.funcionario.list_funcionario import FuncionarioListUseCase as FuncionarioListInterface
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface
from src.domain.models.funcionario_model import Funcionario

class FuncionarioListUseCase(FuncionarioListInterface):
    def __init__(self, funcionario_repository: FuncionarioRepositoryInterface):
        self.funcionario_repository = funcionario_repository
    
    def list(self) -> List[Dict]:
        funcionarios = self.funcionario_repository.findAll()
        return [self.__format_response(funcionario) for funcionario in funcionarios]
    
    def __format_response(self, funcionario: Funcionario) -> Dict:
        response = {
            "type": "Funcionario",
            "id": getattr(funcionario, "id", None),
            "attributes": {
                "nome": getattr(funcionario, "nome", None),
                "cpf": getattr(funcionario, "cpf", None),
                "cargo": getattr(funcionario, "cargo", None),
                "setor_id": getattr(funcionario, "setor_id", None),
                "telefone": getattr(funcionario, "telefone", None),
                "email": getattr(funcionario, "email", None),
                "data_contratacao": getattr(funcionario, "data_contratacao", None)
            }
        }
        return response