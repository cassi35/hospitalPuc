from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
from src.domain.models.setor_model import Setor as SetorDomain
from src.infra.db.entities.setor import Setor as SetorEntity
class SetorRepository(SetorRepositoryInterface):
    pass
