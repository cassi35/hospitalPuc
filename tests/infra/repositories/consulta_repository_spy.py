from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface
from src.domain.models.consulta_model import Consulta as ConsultaDomain 
from typing import List
class ConsultaRepositorySpy(ConsultaRepositoryInterface):
    def __init__(self):
        self.create_consulta_attributes = {}
        self.create_consulta_call_count = 0

        self.update_consulta_attributes = {}
        self.update_consulta_call_count = 0

        self.delete_consulta_attributes = {}
        self.delete_consulta_call_count = 0

        self.findAll_consulta_attributes = {}
        self.findAll_consulta_call_count = 0

        self.findById_consulta_attributes = {}
        self.findById_consulta_call_count = 0

    def create(self, data_hora: str, paciente_id: int, medico_id: int, especialidade_id: int, status: str, observacoes: str) -> None:
        self.create_consulta_attributes = {
            "data_hora": data_hora,
            "paciente_id": paciente_id,
            "medico_id": medico_id,
            "especialidade_id": especialidade_id,
            "status": status,
            "observacoes": observacoes
        }
        self.create_consulta_call_count += 1
    def update(self, id: int, data_hora: str, paciente_id: int, medico_id: int, especialidade_id: int, status: str, observacoes: str) -> None:
        self.update_consulta_attributes = {
            "id": id,
            "data_hora": data_hora,
            "paciente_id": paciente_id,
            "medico_id": medico_id,
            "especialidade_id": especialidade_id,
            "status": status,
            "observacoes": observacoes
        }
        self.update_consulta_call_count += 1
    def delete(self, id: int) -> bool:
        self.delete_consulta_attributes = {"id":id}
        self.delete_consulta_call_count +=1
        return True
    def findById(self, id: int) -> ConsultaDomain:
        self.findById_consulta_attributes = {"id":id}
        self.findById_consulta_call_count +=1
        consulta = ConsultaDomain(
            id=id,
            data_hora="2023-10-10 10:00:00",
            paciente_id=1,
            medico_id=1,
            especialidade_id=1,
            status="Agendada",
            observacoes="Observações de teste"
        )
        return consulta
    def findAll(self) -> List[ConsultaDomain]:
        self.findAll_consulta_attributes = {}
        self.findAll_consulta_call_count +=1
        consulta1 = ConsultaDomain(
            id=1,
            data_hora="2023-10-10 10:00:00",
            paciente_id=1,
            medico_id=1,
            especialidade_id=1,
            status="Agendada",
            observacoes="Observações de teste 1"
        )
        consulta2 = ConsultaDomain(
            id=2,
            data_hora="2023-11-11 11:00:00",
            paciente_id=2,
            medico_id=2,
            especialidade_id=2,
            status="Concluída",
            observacoes="Observações de teste 2"
        )
        return [consulta1, consulta2]
