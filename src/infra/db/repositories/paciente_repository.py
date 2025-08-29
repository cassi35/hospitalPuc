from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from src.domain.models.paciente_model import Paciente as PacienteDomain
from src.infra.db.entities.paciente import Paciente as PacienteEntity
class PacienteRepository(PacienteRepositoryInterface):
    pass
