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
            "id": funcionario.id,
            "attributes": {
                "nome": funcionario.nome,
                "cpf": funcionario.cpf,
                "cargo": funcionario.cargo,
                "setor_id": funcionario.setor_id,
                "telefone": funcionario.telefone,
                "email": funcionario.email,
                "data_contratacao": funcionario.data_contratacao.isoformat() if funcionario.data_contratacao else None
            }
        }
        return response