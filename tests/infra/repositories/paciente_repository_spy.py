from typing import List,Optional
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from src.domain.models.paciente_model import Paciente as PacienteDomain
class PacienteRepositorySpy(PacienteRepositoryInterface):
    def __init__(self):
        self.insert_paciente_attributes = {}
        self.insert_paciente_call_count = 0
        
        self.delete_paciente_attributes = {}
        self.delete_paciente_call_count = 0

        self.select_paciente_attributes = {}
        self.select_paciente_call_count = 0 

        self.udpate_paciente_attributes = {}
        self.udpate_paciente_call_count = 0 

        self.delete_paciente_return = True
    def insert_paciente(self,nome:str,cpf:str,data_nascimento:str,sexo:str,telefone:str,alergia:str,contato_emergencia:str,endereco_id:int,convenio_id:int) -> None:
        self.insert_paciente_attributes = {
            'nome': nome,
            'cpf': cpf,
            'data_nascimento': data_nascimento,
            'sexo': sexo,
            'telefone': telefone,
            'alergia': alergia,
            'contato_emergencia': contato_emergencia,
            'endereco_id': endereco_id,
            'convenio_id': convenio_id
        }
        self.insert_paciente_call_count += 1
    def delete_paciente(self,id:int) -> bool:
        self.delete_paciente_attributes = {"id":id}
        self.delete_paciente_call_count+=1 
        return self.delete_paciente_return
    def select_paciente(self,id:int)-> Optional[PacienteDomain]:
        self.select_paciente_attributes = {"id":id}
        self.select_paciente_call_count +=1
        paciente = PacienteDomain(
            id=id,
            nome="Paciente Teste",
            data_nascimento="2000-01-01",
            cpf="12345678900",
            sexo="M",
            telefone="(11) 99999-9999",
            alergia="Nenhuma",
            contato_emergencia="(11) 98888-8888",
            endereco_id=1,
            convenio_id=1
        )
        return paciente
    def udpate_paciente(self, id:int, nome:str, cpf:str, data_nascimento:str, sexo:str, telefone:str, alergia:str, contato_emergencia:str, endereco_id:int, convenio_id:int)-> None:
        self.udpate_paciente_attributes = {
            'id': id,
            'nome': nome,
            'cpf': cpf,
            'data_nascimento': data_nascimento,
            'sexo': sexo,
            'telefone': telefone,
            'alergia': alergia,
            'contato_emergencia': contato_emergencia,
            'endereco_id': endereco_id,
            'convenio_id': convenio_id
        }
        self.udpate_paciente_call_count+=1
    def list_pacientes(self)-> List[PacienteDomain]:
        paciente1 = PacienteDomain(
            id=1,
            nome="Paciente A",
            data_nascimento="1990-01-01",
            cpf="11111111111",
            sexo="F",
            telefone="(11) 91111-1111",
            alergia="Nenhuma",
            contato_emergencia="(11) 92222-2222",
            endereco_id=1,
            convenio_id=1
        )
        paciente2 = PacienteDomain(
            id=2,
            nome="Paciente B",
            data_nascimento="1985-05-05",
            cpf="22222222222",
            sexo="M",
            telefone="(11) 93333-3333",
            alergia="Penicilina",
            contato_emergencia="(11) 94444-4444",
            endereco_id=2,
            convenio_id=2
        )
        return [paciente1, paciente2]
    