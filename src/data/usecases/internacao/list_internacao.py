from typing import List, Dict
from src.domain.usecases.internacao.list_internacao import InternacaoListUseCase as InternacaoListInterface
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface
from src.domain.models.internacao_model import Internacao

class InternacaoListUseCase(InternacaoListInterface):
    def __init__(self, internacao_repository: InternacaoRepositoryInterface):
        self.internacao_repository = internacao_repository

    def list(self) -> List[Dict]:
        internacoes = self.internacao_repository.findAll()
        return [self.__format_response(internacao) for internacao in internacoes]

    def __format_response(self, internacao: Internacao) -> Dict:
        response = {
            "type": "Internacao",
            "id": internacao.id,
            "attributes": {
                "paciente_id": internacao.paciente_id,
                "medico_id": internacao.medico_id,
                "leito_id": internacao.leito_id,
                "data_entrada": str(internacao.data_entrada) if internacao.data_entrada else None,
                "status": internacao.status
            }
        }
        return response