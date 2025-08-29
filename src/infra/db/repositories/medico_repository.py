from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.domain.models.medico_model import Medico as MedicoDomain
from src.infra.db.entities.medico import Medico as MedicoEntity
class MedicoRepository(MedicoRepositoryInterface):
    pass
