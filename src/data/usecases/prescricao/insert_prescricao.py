from typing import Dict
from src.domain.usecases.prescricao.insert_prescricao import PrescricaoInsertUseCase as PrescricaoInsertInterface
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from src.domain.models.prescricao_model import Prescricao
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from datetime import datetime

class PrescricaoInsertUseCase(PrescricaoInsertInterface):
    def __init__(
        self, 
        prescricao_repository: PrescricaoRepositoryInterface,
        paciente_repository: PacienteRepositoryInterface,
        medico_repository: MedicoRepositoryInterface,
        medicamento_repository: MedicamentoRepositoryInterface
    ):
        self.prescricao_repository = prescricao_repository
        self.paciente_repository = paciente_repository
        self.medico_repository = medico_repository
        self.medicamento_repository = medicamento_repository

    def insert(self, prescricao: Prescricao) -> Dict:
        self.__validate_informations(prescricao)
        self.__insert_prescricao(prescricao)
        return self.__format_response(prescricao)

    def __validate_informations(self, prescricao: Prescricao) -> None:
        # Validar paciente_id
        if not prescricao.paciente_id:
            raise HttpBadRequestError("ID do paciente é obrigatório")
        if not isinstance(prescricao.paciente_id, int) or prescricao.paciente_id <= 0:
            raise HttpBadRequestError("ID do paciente deve ser um número positivo")
        
        paciente = self.paciente_repository.select_paciente(id=prescricao.paciente_id)
        if not paciente:
            raise HttpNotFoundError("Paciente não encontrado")

        # Validar medico_id
        if not prescricao.medico_id:
            raise HttpBadRequestError("ID do médico é obrigatório")
        if not isinstance(prescricao.medico_id, int) or prescricao.medico_id <= 0:
            raise HttpBadRequestError("ID do médico deve ser um número positivo")
        
        medico = self.medico_repository.findById(prescricao.medico_id)
        if not medico:
            raise HttpNotFoundError("Médico não encontrado")

        # Validar medicamento_id
        if not prescricao.medicamento_id:
            raise HttpBadRequestError("ID do medicamento é obrigatório")
        if not isinstance(prescricao.medicamento_id, int) or prescricao.medicamento_id <= 0:
            raise HttpBadRequestError("ID do medicamento deve ser um número positivo")
        
        medicamento = self.medicamento_repository.findById(prescricao.medicamento_id)
        if not medicamento:
            raise HttpNotFoundError("Medicamento não encontrado")

        # Validar data_prescricao
        if not prescricao.data_prescricao:
            raise HttpBadRequestError("Data da prescrição é obrigatória")
        
        try:
            prescricao_date = datetime.strptime(str(prescricao.data_prescricao), '%Y-%m-%d').date()
            today = datetime.now().date()
            if prescricao_date > today:
                raise HttpBadRequestError("Data da prescrição não pode ser futura")
        except ValueError:
            raise HttpBadRequestError("Data da prescrição inválida")

        # Validar dosagem
        if not prescricao.dosagem:
            raise HttpBadRequestError("Dosagem é obrigatória")
        if not isinstance(prescricao.dosagem, int) or prescricao.dosagem <= 0:
            raise HttpBadRequestError("Dosagem deve ser um número positivo")

        # Validar frequencia
        if not prescricao.frequencia:
            raise HttpBadRequestError("Frequência é obrigatória")
        if not isinstance(prescricao.frequencia, int) or prescricao.frequencia <= 0:
            raise HttpBadRequestError("Frequência deve ser um número positivo")

    def __insert_prescricao(self, prescricao: Prescricao) -> None:
        self.prescricao_repository.create(
            paciente_id=prescricao.paciente_id,
            medico_id=prescricao.medico_id,
            data_prescricao=prescricao.data_prescricao,
            medicamento_id=prescricao.medicamento_id,
            dosagem=prescricao.dosagem,
            frequencia=prescricao.frequencia
        )

    def __format_response(self, prescricao: Prescricao) -> Dict:
        return {
            "type": "Prescricao",
            "count": 1,
            "attributes": {
                "paciente_id": prescricao.paciente_id,
                "medico_id": prescricao.medico_id,
                "data_prescricao": str(prescricao.data_prescricao),
                "medicamento_id": prescricao.medicamento_id,
                "dosagem": prescricao.dosagem,
                "frequencia": prescricao.frequencia
            }
        }