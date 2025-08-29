from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface
from src.domain.models.consulta_model import Consulta as ConsultaDomain
from src.infra.db.entities.consulta import Consulta as ConsultaEntity
class ConsultaRepository(ConsultaRepositoryInterface):
    pass
