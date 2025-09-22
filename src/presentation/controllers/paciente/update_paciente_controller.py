from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.paciente.update_paciente import PacienteUpdateUseCase as PacienteUpdateInterface
from src.domain.models.paciente_model import Paciente as PacienteDomain
class PacienteUpdateController(ControllerInterface):
    def __init__(self,usecase:PacienteUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        paciente_id = int(http_request.path_params["id"])
        paciente = PacienteDomain(**http_request.body) 
        paciente.id = paciente_id
        response = self.usecase.update(
            paciente_id=paciente_id,
            paciente=paciente
        )
        return HTTPResponse(status_code=200,body=response)
