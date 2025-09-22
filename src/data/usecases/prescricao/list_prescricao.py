from typing import Dict, List
from src.domain.usecases.prescricao.list_prescricao import PrescricaoListUseCase as PrescricaoListInterface
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface
from src.domain.models.prescricao_model import Prescricao

class PrescricaoListUseCase(PrescricaoListInterface):
    def __init__(self, prescricao_repository: PrescricaoRepositoryInterface):
        self.prescricao_repository = prescricao_repository

    def list(self) -> Dict:
        prescricoes = self.__list_prescricoes()
        return self.__format_response(prescricoes)

    def __list_prescricoes(self) -> List[Prescricao]:
        return self.prescricao_repository.findAll()

    def __format_response(self, prescricoes: List[Prescricao]) -> Dict:
        return {
            "type": "Prescricoes",
            "count": len(prescricoes),
            "attributes": [
                {
                    "id": prescricao.id,
                    "paciente_id": prescricao.paciente_id,
                    "medico_id": prescricao.medico_id,
                    "data_prescricao": str(prescricao.data_prescricao) if prescricao.data_prescricao else None,
                    "medicamento_id": prescricao.medicamento_id,
                    "dosagem": prescricao.dosagem,
                    "frequencia": prescricao.frequencia
                }
                for prescricao in prescricoes
            ]
        }