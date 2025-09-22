from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.medico.delete_medico import MedicoDeleteUseCase as MedicoDeleteInterface
class MedicoDeleteController(ControllerInterface): 
    def __init__(self,usecase:MedicoDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        medico_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            medico_id=medico_id
        )
        return HTTPResponse(status_code=200,body=response)
