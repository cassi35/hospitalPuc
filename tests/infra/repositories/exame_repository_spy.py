from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface
from src.domain.models.exame_model import Exame as ExameDomain
from typing import List 
class ExameRepositorySpy(ExameRepositoryInterface):
    def __init__(self):
        self.create_exame_attributes = {}
        self.create_exame_call_count = 0

        self.update_exame_attributes = {}
        self.update_exame_call_count = 0

        self.delete_exame_attributes = {}
        self.delete_exame_call_count = 0

        self.findAll_exame_attributes = {}
        self.findAll_exame_call_count = 0

        self.findById_exame_attributes = {}
        self.findById_exame_call_count = 0
    def create(self, tipo_exame: str, data_exame: str, paciente_id: int, medico_id: int, resultado: str, status: str) -> None:
        self.create_exame_attributes = {
            "tipo_exame": tipo_exame,
            "data_exame": data_exame,
            "paciente_id": paciente_id,
            "medico_id": medico_id,
            "resultado": resultado,
            "status": status
        }
        self.create_exame_call_count += 1
    def update(self, id: int, tipo_exame: str, data_exame: str, paciente_id: int, medico_id: int, resultado: str, status: str) -> None:
        self.update_exame_attributes = {
            "id": id,
            "tipo_exame": tipo_exame,
            "data_exame": data_exame,
            "paciente_id": paciente_id,
            "medico_id": medico_id,
            "resultado": resultado,
            "status": status
        }
        self.update_exame_call_count += 1
    def delete(self, id: int) -> bool:
        self.delete_exame_attributes = {"id":id}
        self.delete_exame_call_count +=1
        return True
    def findById(self, id: int) -> ExameDomain:
        self.findById_exame_attributes = {"id":id}
        self.findById_exame_call_count +=1
        exame = ExameDomain(
            id=id,
            tipo_exame="Tipo Teste",
            data_exame="2023-10-10",
            paciente_id=1,
            medico_id=1,
            resultado="Resultado Teste",
            status="Pendente"
        )
        return exame
    def findAll(self) -> List[ExameDomain]:
        self.findAll_exame_attributes = {}
        self.findAll_exame_call_count +=1
        exame1 = ExameDomain(
            id=1,
            tipo_exame="Tipo A",
            data_exame="2023-10-10",
            paciente_id=1,
            medico_id=1,
            resultado="Resultado A",
            status="Pendente"
        )
        exame2 = ExameDomain(
            id=2,
            tipo_exame="Tipo B",
            data_exame="2023-11-11",
            paciente_id=2,
            medico_id=2,
            resultado="Resultado B",
            status="Concluído"
        )
        return [exame1, exame2]