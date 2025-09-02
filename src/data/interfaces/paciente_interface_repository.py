from abc import ABC,abstractmethod
from typing import List
from src.domain.models.paciente_model import Paciente
class PacienteRepositoryInterface(ABC):pass
@abstractmethod
def insert_paciente(self,nome:str,cpf:str,data_nascimento:str,sexo:str,telefone:str,alergia:str,contato_emergencia:str,endereco_id:str,convenio_id:str) -> None:
        pass
def select_paciente(self, id: int) -> Paciente:
        pass
def update_paciente(self, id: int, nome: str, cpf: str, data_nascimento: str, sexo: str, telefone: str, alergia: str, contato_emergencia: str, endereco_id: int, convenio_id: int) -> None:
        pass
def delete_paciente(self, id: int) -> bool:
        pass
def list_pacientes(self) -> List[Paciente]:
        pass