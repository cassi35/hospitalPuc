from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.leito.update_leito import LeitoUpdateUseCase as LeitoUpdateInterface
from src.domain.models.leito_model import Leito as LeitoDomain
class LeitoUpdateController(ControllerInterface):
    def __init__(self,usecase:LeitoUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        leito_id = int(http_request.path_params["id"])
        leito = LeitoDomain(**http_request.body) 
        leito.id = leito_id
        response = self.usecase.update(
            leito_id=leito_id,
            leito=leito
        )
        return HTTPResponse(status_code=200,body=response)
