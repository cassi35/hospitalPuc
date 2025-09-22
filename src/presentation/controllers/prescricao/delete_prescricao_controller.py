from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.prescricao.delete_prescricao import PrescricaoDeleteUseCase as PrescricaoDeleteInterface
class PrescricaoDeleteController(ControllerInterface): 
    def __init__(self,usecase:PrescricaoDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        prescricao_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            prescricao_id=prescricao_id
        )
        return HTTPResponse(status_code=200,body=response)
