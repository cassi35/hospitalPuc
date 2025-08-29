from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface
from src.domain.models.exame_model import Exame as ExameDomain
from src.infra.db.entities.exame import Exame as ExameEntity
class ExameRepository(ExameRepositoryInterface):
    pass
