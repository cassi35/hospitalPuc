from typing import Dict
from datetime import datetime
from src.domain.usecases.exame.insert_exame import ExameInsertUseCase as ExameInsertInterface
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.domain.models.exame_model import Exame
from src.errors.types.http_bad_request import HttpBadRequestError

class ExameInsertUseCase(ExameInsertInterface):
    def __init__(
        self,
        exame_repository: ExameRepositoryInterface,
        paciente_repository: PacienteRepositoryInterface,
        medico_repository: MedicoRepositoryInterface
    ):
        self.exame_repository = exame_repository
        self.paciente_repository = paciente_repository
        self.medico_repository = medico_repository

    def insert(self, exame: Exame) -> Dict:
        self.__validate_informations(exame)
        # create(tipo_exame, data_exame, paciente_id, medico_id, resultado, status)
        self.exame_repository.create(
            exame.tipo_exame,
            exame.data_exame,
            exame.paciente_id,
            exame.medico_id,
            exame.resultado,
            exame.status
        )
        return self.__format_response(exame)

    def __validate_informations(self, exame: Exame) -> None:
        # tipo_exame (obrigatório, não vazio)
        if not exame.tipo_exame or str(exame.tipo_exame).strip() == "":
            raise HttpBadRequestError("tipo_exame é obrigatório")

        # data_exame (obrigatória, data válida, ≤ hoje)
        if not exame.data_exame:
            raise HttpBadRequestError("data_exame é obrigatória")
        try:
            data = datetime.strptime(str(exame.data_exame), "%Y-%m-%d").date()
            if data > datetime.now().date():
                raise HttpBadRequestError("data_exame não pode ser futura")
        except ValueError:
            raise HttpBadRequestError("data_exame inválida")

        # paciente_id (FK existente)
        if not isinstance(exame.paciente_id, int) or exame.paciente_id <= 0:
            raise HttpBadRequestError("paciente_id inválido")
        if not self.paciente_repository.select_paciente(exame.paciente_id):
            raise HttpBadRequestError("Paciente não encontrado")

        # medico_id (FK existente)
        if not isinstance(exame.medico_id, int) or exame.medico_id <= 0:
            raise HttpBadRequestError("medico_id inválido")
        if not self.medico_repository.findById(exame.medico_id):
            raise HttpBadRequestError("Médico não encontrado")

        # resultado (opcional) -> sem validação extra

        # status
        if exame.status not in ["solicitado", "em andamento", "concluído"]:
            raise HttpBadRequestError("status inválido")

    def __format_response(self, exame: Exame) -> Dict:
        return {
            "type": "Exame",
            "count": 1,
            "attributes": {
                "tipo_exame": exame.tipo_exame,
                "data_exame": exame.data_exame,
                "paciente_id": exame.paciente_id,
                "medico_id": exame.medico_id,
                "resultado": exame.resultado,
                "status": exame.status
            }
        }