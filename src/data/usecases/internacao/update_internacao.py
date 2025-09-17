from typing import Dict
from src.domain.usecases.internacao.update_internacao import InternacaoUpdateUseCase as InternacaoUpdateInterface
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface
from src.infra.db.entities.internacao import Internacao
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from datetime import datetime

class InternacaoUpdateUseCase(InternacaoUpdateInterface):
    def __init__(
        self,
        internacao_repository: InternacaoRepositoryInterface,
        paciente_repository: PacienteRepositoryInterface,
        medico_repository: MedicoRepositoryInterface,
        leito_repository: LeitoRepositoryInterface
    ):
        self.internacao_repository = internacao_repository
        self.paciente_repository = paciente_repository
        self.medico_repository = medico_repository
        self.leito_repository = leito_repository

    def update(self, internacao_id: int, internacao: Internacao) -> Dict:
        self.__validate_internacao_id(internacao_id)
        self.__exists_internacao(internacao_id)
        self.__validate_informations(internacao)
        self.internacao_repository.update_internacao(
            internacao_id=internacao_id,
            paciente_id=internacao.paciente_id,
            medico_id=internacao.medico_id,
            leito_id=internacao.leito_id,
            data_entrada=internacao.data_entrada,
            status=internacao.status
        )
        return self.__format_response(internacao)

    def __validate_internacao_id(self, internacao_id: int) -> None:
        if not isinstance(internacao_id, int) or internacao_id <= 0:
            raise HttpBadRequestError("ID da internação deve ser um número positivo")

    def __exists_internacao(self, internacao_id: int) -> None:
        if not self.internacao_repository.select_internacao(internacao_id):
            raise HttpNotFoundError("Internação não encontrada")

    def __validate_informations(self, internacao: Internacao) -> None:
        # paciente_id
        if not internacao.paciente_id or not isinstance(internacao.paciente_id, int) or internacao.paciente_id <= 0:
            raise HttpBadRequestError("ID do paciente inválido")
        if not self.paciente_repository.select_paciente(internacao.paciente_id):
            raise HttpBadRequestError("Paciente não encontrado")

        # medico_id
        if not internacao.medico_id or not isinstance(internacao.medico_id, int) or internacao.medico_id <= 0:
            raise HttpBadRequestError("ID do médico inválido")
        if not self.medico_repository.findById(internacao.medico_id):
            raise HttpBadRequestError("Médico não encontrado")

        # leito_id
        if not internacao.leito_id or not isinstance(internacao.leito_id, int) or internacao.leito_id <= 0:
            raise HttpBadRequestError("ID do leito inválido")
        leito = self.leito_repository.findById(internacao.leito_id)
        if not leito:
            raise HttpBadRequestError("Leito não encontrado")
        if hasattr(leito, "status") and getattr(leito, "status", None) == "ocupado":
            raise HttpBadRequestError("Leito já está ocupado")

        # data_entrada
        if not internacao.data_entrada:
            raise HttpBadRequestError("Data de entrada é obrigatória")
        try:
            data_entrada = datetime.strptime(str(internacao.data_entrada), '%Y-%m-%d').date()
            today = datetime.now().date()
            if data_entrada > today:
                raise HttpBadRequestError("Data de entrada não pode ser futura")
        except ValueError:
            raise HttpBadRequestError("Data de entrada inválida")

        # status
        if internacao.status not in ["em andamento", "alta", "obito"]:
            raise HttpBadRequestError("Status inválido")

    def __format_response(self, internacao: Internacao) -> Dict:
        return {
            "type": "Internacao",
            "count": 1,
            "attributes": {
                "paciente_id": internacao.paciente_id,
                "medico_id": internacao.medico_id,
                "leito_id": internacao.leito_id,
                "data_entrada": str(internacao.data_entrada),
                "status": internacao.status
            }
        }