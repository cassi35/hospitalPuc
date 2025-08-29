from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface
from src.domain.models.financeiro_model import Financeiro as FinanceiroDomain
from src.infra.db.entities.financeiro import Financeiro as FinanceiroEntity
class FinanceiroRepository(FinanceiroRepositoryInterface):
    pass
