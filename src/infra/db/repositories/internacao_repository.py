from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface
from src.domain.models.internacao_model import Internacao as InternacaoDomain
from src.infra.db.entities.internacao import Internacao as InternacaoEntity
class InternacaoRepository(InternacaoRepositoryInterface):
    pass
