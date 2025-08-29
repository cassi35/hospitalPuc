from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface
from src.domain.models.prescricao_model import Prescricao as PrescricaoDomain
from src.infra.db.entities.prescricao import Prescricao as PrescricaoEntity
class PrescricaoRepository(PrescricaoRepositoryInterface):
    pass
