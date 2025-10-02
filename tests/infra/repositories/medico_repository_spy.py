from typing import List,Optional
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.domain.models.medico_model import Medico as MedicoDomain
class MedicoRepositorySpy(MedicoRepositoryInterface):
    def __init__(self):
        self.create_medico_attributes = {}
        self.create_medico_call_count = 0

        self.update_medico_attributes = {}
        self.update_medico_call_count = 0

        self.delete_medico_attributes = {}
        self.delete_medico_call_count = 0
        self.delete_medico_return = True

        self.findById_medico_attributes = {}
        self.findById_medico_call_count = 0

    def create(self, nome:str, cpf:str, especialidade_id:int, telefone:str, email:str, status:str) -> None:
        self.create_medico_attributes = {
            'nome': nome,
            'cpf': cpf,
            'especialidade_id': especialidade_id,
            'telefone': telefone,
            'email': email,
            'status': status
        }
        self.create_medico_call_count += 1

    def update(self, id:int, nome:str, cpf:str, especialidade_id:int, telefone:str, email:str, status:str) -> None:
        self.update_medico_attributes = {
            'id': id,
            'nome': nome,
            'cpf': cpf,
            'especialidade_id': especialidade_id,
            'telefone': telefone,
            'email': email,
            'status': status
        }
        self.update_medico_call_count += 1

    def delete(self, id:int) -> bool:
        self.delete_medico_attributes = {'id': id}
        self.delete_medico_call_count += 1
        return self.delete_medico_return

    def findById(self, id:int) -> Optional[MedicoDomain]:
        self.findById_medico_attributes = {'id': id}
        self.findById_medico_call_count += 1
        medico = MedicoDomain(
            id=id,
            nome="Dr. Teste",
            cpf="123.456.789-00",
            especialidade_id=1,
            telefone="(11) 91234-5678",
            email="email@medico.com",
            status="Ativo"

        )
        return medico
    def findAll(self)-> List[MedicoDomain]:
        medico1 = MedicoDomain(
            id=1,
            nome="Dr. A",
            cpf="111.111.111-11",
            especialidade_id=1,
            telefone="(11) 91111-1111",
            email="email@medico.com",
            status="Ativo"
        )
        medico2 = MedicoDomain(
            id=2,
            nome="Dr. B",
            cpf="222.222.222-22",
            especialidade_id=2,
            telefone="(11) 92222-2222",
            email="email@medico.com",
            status="Ativo"
        )
        return [medico1, medico2]
    def findByCpf(self, cpf:str)-> MedicoDomain:
        medico = MedicoDomain(
            id=1,
            nome="Dr. Teste",
            cpf=cpf,
            especialidade_id=1,
            telefone="(11) 91234-5678",
            email="medico@gmail.com",
            status="Ativo"
        )
        return medico
    def findByEmail(self, email:str)-> MedicoDomain:
        medico = MedicoDomain(
            id=1,
            nome="Dr. Teste",
            cpf="123.456.789-00",
            especialidade_id=1,
            telefone="(11) 91234-5678",
            email=email,
            status="Ativo"
        )
        return medico