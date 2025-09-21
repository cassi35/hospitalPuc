from typing import List
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface
from src.domain.models.prescricao_model import Prescricao as PrescricaoDomain

class PrescricaoRepository(PrescricaoRepositoryInterface):
    
    def __init__(self):
        self.create_prescricao_attributes = {}
        self.create_prescricao_call_count = 0

        self.update_precricao_attributes = {}
        self.update_prescricao_call_count = 0

        self.delete_prescricao_attributes = {}
        self.delete_prescricao_call_count = 0

        self.findAll_prescricao_attributes = {}
        self.findAll_prescricao_call_count = 0

        self.findById_prescricao_attributes = {}
        self.findById_prescricao_call_count = 0



    def create(self, paciente_id: int, medico_id: int, data_prescricao: str, medicamento_id: int, dosagem: int, frequencia: int) -> None:
        prescricao = {
            "paciente_id": paciente_id,
            "medico_id": medico_id,
            "data_prescricao": data_prescricao,
            "medicamento_id": medicamento_id,
            "dosagem": dosagem,
            "frequencia": frequencia
        }
        self.create_prescricao_attributes = prescricao
        self.create_prescricao_call_count += 1

    def update(self, id: int, paciente_id: int, medico_id: int, data_prescricao: str, medicamento_id: int, dosagem: int, frequencia: int) -> None:
        prescricao = {
            "id": id,
            "paciente_id": paciente_id,
            "medico_id": medico_id,
            "data_prescricao": data_prescricao,
            "medicamento_id": medicamento_id,
            "dosagem": dosagem,
            "frequencia": frequencia
        }
        self.update_prescricao_attributes = prescricao
        self.update_prescricao_call_count += 1

    def delete(self, id: int) -> bool:
        self.delete_prescricao_attributes = {"id": id}
        self.delete_prescricao_call_count += 1
        return True
    
    def findById(self, id: int) -> PrescricaoDomain:
        self.findById_prescricao_attributes = {"id": id}
        self.findById_prescricao_call_count += 1
        return PrescricaoDomain(
                   id=id,
                   paciente_id=1,
                  medico_id=1,
                 data_prescricao="2025-01-01",
                 medicamento_id=1,
                  dosagem=500,
                  frequencia=3
              )
    def findAll(self) -> List[PrescricaoDomain]:
        self.findAll_prescricao_call_count += 1
        return [PrescricaoDomain(
            id=1,
            paciente_id=1,
            medico_id=1,
            data_prescricao="2025-01-01",
            medicamento_id=1,
            dosagem=500,
            frequencia=3
        )]