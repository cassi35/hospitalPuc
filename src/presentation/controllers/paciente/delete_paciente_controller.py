from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.paciente.delete_paciente import PacienteDeleteUseCase as PacienteDeleteInterface
class PacienteDeleteController(ControllerInterface): 
    def __init__(self,usecase:PacienteDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        paciente_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            paciente_id=paciente_id
        )
        return HTTPResponse(status_code=200,body=response)
