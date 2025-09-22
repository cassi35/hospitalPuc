from typing import List, Dict
from src.domain.usecases.paciente.list_paciente import PacienteListUseCase as PacienteListInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from src.domain.models.paciente_model import Paciente
class PacienteListUseCase(PacienteListInterface):
    def __init__(self, paciente_repository: PacienteRepositoryInterface):
        self.paciente_repository = paciente_repository
    
    def list(self) -> List[Dict]:
        pacientes = self.paciente_repository.list_pacientes()
        return [self.__format_response(paciente) for paciente in pacientes]
    def __format_response(self,paciente:Paciente) -> Dict:
        response = {
            "type": "Paciente",
            "id": paciente.id,
            "attributes": {
                "nome": paciente.nome,
                "cpf": paciente.cpf,
                "data_nascimento": paciente.data_nascimento,
                "sexo": paciente.sexo,
                "telefone": paciente.telefone,
                "contato_emergencia": paciente.contato_emergencia,
                "alergia": paciente.alergia,
                "endereco_id": paciente.endereco_id,
                "convenio_id": paciente.convenio_id
            }
        }
        return response
