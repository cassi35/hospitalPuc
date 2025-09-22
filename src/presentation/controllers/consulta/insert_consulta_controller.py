from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.consulta.insert_consulta import ConsultaInsertUseCase as ConsultaInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.consulta_model import Consulta as ConsultaDomain
class ConsultaInsertController(ControllerInterface):
    def __init__(self,usecase:ConsultaInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        consulta = ConsultaDomain(**http_request.body)
        response = self.usecase.insert(
            consulta=consulta
        )
        return HTTPResponse(status_code=200,body=response)
