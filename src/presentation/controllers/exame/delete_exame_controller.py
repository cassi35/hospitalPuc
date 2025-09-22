from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.exame.delete_exame import ExameDeleteUseCase as ExameDeleteInterface
class ExameDeleteController(ControllerInterface): 
    def __init__(self,usecase:ExameDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        exame_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            exame_id=exame_id
        )
        return HTTPResponse(status_code=200,body=response)
