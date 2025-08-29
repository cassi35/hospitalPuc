from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface
from src.domain.models.especialidade_model import Especialidade as EspecialidadeDomain
from src.infra.db.entities.especialidade import Especialidade as EspecialidadeEntity
class EspecialidadeRepository(EspecialidadeRepositoryInterface):
    pass
