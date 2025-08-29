from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from src.domain.models.medicamento_model import Medicamento as MedicamentoDomain
from src.infra.db.entities.medicamento import Medicamento as MedicamentoEntity
class MedicamentoRepository(MedicamentoRepositoryInterface):
    pass
