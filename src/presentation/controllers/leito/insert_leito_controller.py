from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.leito.insert_leito import LeitoInsertUseCase as LeitoInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.leito_model import Leito as LeitoDomain
class LeitoInsertController(ControllerInterface):
    def __init__(self,usecase:LeitoInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        leito = LeitoDomain(**http_request.body)
        response = self.usecase.insert(
            leito=leito
        )
        return HTTPResponse(status_code=200,body=response)
