from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface
from src.domain.models.funcionario_model import Funcionario as FuncionarioDomain
from src.infra.db.entities.funcionario import Funcionario as FuncionarioEntity
class FuncionarioRepository(FuncionarioRepositoryInterface):
    pass
