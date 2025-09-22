from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.endereco.insert_endereco import EnderecoInsertUseCase as EnderecoInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.endereco_model import Endereco as EnderecoDomain
class EnderecoInsertController(ControllerInterface):
    def __init__(self,usecase:EnderecoInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        endereco = EnderecoDomain(**http_request.body)
        response = self.usecase.insert(
            endereco=endereco
        )
        return HTTPResponse(status_code=200,body=response)