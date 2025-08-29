from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface
from src.domain.models.leito_model import Leito as LeitoDomain
from src.infra.db.entities.leito import Leito as LeitoEntity
class LeitoRepository(LeitoRepositoryInterface):
    pass
