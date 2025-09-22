from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.paciente.insert_paciente import PacienteInsertUseCase as PacienteInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.paciente_model import Paciente as PacienteDomain
class PacienteInsertController(ControllerInterface):
    def __init__(self,usecase:PacienteInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        paciente = PacienteDomain(**http_request.body)
        response = self.usecase.insert(
            paciente=paciente
        )
        return HTTPResponse(status_code=200,body=response)
