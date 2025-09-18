from typing import List, Optional
from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface
from src.domain.models.internacao_model import Internacao as InternacaoDomain

class InternacaoRepositorySpy(InternacaoRepositoryInterface):
    def __init__(self):
        self.create_attributes = {}
        self.create_call_count = 0

        self.update_attributes = {}
        self.update_call_count = 0

        self.delete_attributes = {}
        self.delete_call_count = 0
        self.delete_return = True

        self.findById_attributes = {}
        self.findById_call_count = 0
        self.findById_return = None

        self.findAll_attributes = {}
        self.findAll_call_count = 0
        self.findAll_return = []

        self.findByPaciente_attributes = {}
        self.findByPaciente_call_count = 0
        self.findByPaciente_return = []

    def create(self, paciente_id: int, medico_id: int, leito_id: int, data_entrada: str, status: str) -> None:
        self.create_attributes = {
            "paciente_id": paciente_id,
            "medico_id": medico_id,
            "leito_id": leito_id,
            "data_entrada": data_entrada,
            "status": status
        }
        self.create_call_count += 1

    def update(self, id: int, paciente_id: int, medico_id: int, leito_id: int, data_entrada: str, status: str) -> None:
        self.update_attributes = {
            "id": id,
            "paciente_id": paciente_id,
            "medico_id": medico_id,
            "leito_id": leito_id,
            "data_entrada": data_entrada,
            "status": status
        }
        self.update_call_count += 1

    def delete(self, id: int) -> bool:
        self.delete_attributes = {"id": id}
        self.delete_call_count += 1
        return self.delete_return

    def findById(self, id: int) -> InternacaoDomain:
        self.findById_attributes = {"id": id}
        self.findById_call_count += 1
        internacao = InternacaoDomain(
            id=id,
            paciente_id=1,
            medico_id=1,
            leito_id=101,
            data_entrada="2023-10-01",
            status="Ativo"
        )
        return internacao

    def findAll(self) -> List[InternacaoDomain]:
        self.findAll_attributes = {}
        self.findAll_call_count += 1
        internacao1 = InternacaoDomain(
            id=1,
            paciente_id=1,
            medico_id=1,
            leito_id=101,
            data_entrada="2023-10-01",
            status="Ativo"
        )
        internacao2 = InternacaoDomain(
            id=2,
            paciente_id=2,
            medico_id=2,
            leito_id=102,
            data_entrada="2023-10-02",
            status="Ativo"
        )
        return [internacao1, internacao2]

    def findByPaciente(self, paciente_id: int) -> List[InternacaoDomain]:
        self.findByPaciente_attributes = {"paciente_id": paciente_id}
        self.findByPaciente_call_count += 1
        internacao1 = InternacaoDomain(
            id=1,
            paciente_id=1,
            medico_id=1,
            leito_id=101,
            data_entrada="2023-10-01",
            status="Ativo"
        )
        return [internacao1]

