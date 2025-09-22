
from typing import Dict
from datetime import datetime
from src.domain.usecases.consulta.insert_consulta import ConsultaInsertUseCase as ConsultaInsertInterface
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface
from src.domain.models.consulta_model import Consulta
from src.errors.types.http_bad_request import HttpBadRequestError

class ConsultaInsertUseCase(ConsultaInsertInterface):
    def __init__(
        self,
        consulta_repository: ConsultaRepositoryInterface,
        paciente_repository: PacienteRepositoryInterface,
        medico_repository: MedicoRepositoryInterface,
        especialidade_repository: EspecialidadeRepositoryInterface
    ):
        self.consulta_repository = consulta_repository
        self.paciente_repository = paciente_repository
        self.medico_repository = medico_repository
        self.especialidade_repository = especialidade_repository

    def insert(self, consulta: Consulta) -> Dict:
        self.__validate_informations(consulta)
        # create(data_hora, paciente_id, medico_id, especialidade_id, status, observacoes)
        self.consulta_repository.create(
            consulta.data_hora,
            consulta.paciente_id,
            consulta.medico_id,
            consulta.especialidade_id,
            consulta.status,
            consulta.observacoes
        )
        return self.__format_response(consulta)

    def __validate_informations(self, consulta: Consulta) -> None:
        # data_hora (obrigatória, data válida, >= hoje)
        if not consulta.data_hora:
            raise HttpBadRequestError("data_hora é obrigatória")
        try:
            data = datetime.strptime(str(consulta.data_hora), "%Y-%m-%d").date()
            if data < datetime.now().date():
                raise HttpBadRequestError("data_hora deve ser hoje ou futura")
        except ValueError:
            raise HttpBadRequestError("data_hora inválida")

        # paciente_id
        if not isinstance(consulta.paciente_id, int) or consulta.paciente_id <= 0:
            raise HttpBadRequestError("paciente_id inválido")
        if not self.paciente_repository.select_paciente(consulta.paciente_id):
            raise HttpBadRequestError("Paciente não encontrado")

        # medico_id
        if not isinstance(consulta.medico_id, int) or consulta.medico_id <= 0:
            raise HttpBadRequestError("medico_id inválido")
        if not self.medico_repository.findById(consulta.medico_id):
            raise HttpBadRequestError("Médico não encontrado")

        # especialidade_id
        if not isinstance(consulta.especialidade_id, int) or consulta.especialidade_id <= 0:
            raise HttpBadRequestError("especialidade_id inválido")
        if not self.especialidade_repository.findById(consulta.especialidade_id):
            raise HttpBadRequestError("Especialidade não encontrada")

        # status
        if consulta.status not in ["ativo", "nao ativo"]:
            raise HttpBadRequestError("status inválido")

        # observacoes (opcional, máx 100)
        if consulta.observacoes is not None and len(str(consulta.observacoes)) > 100:
            raise HttpBadRequestError("observacoes deve ter no máximo 100 caracteres")

    def __format_response(self, consulta: Consulta) -> Dict:
        return {
            "type": "Consulta",
            "count": 1,
            "attributes": {
                "data_hora": str(consulta.data_hora),
                "paciente_id": consulta.paciente_id,
                "medico_id": consulta.medico_id,
                "especialidade_id": consulta.especialidade_id,
                "status": consulta.status,
                "observacoes": consulta.observacoes
            }
        }