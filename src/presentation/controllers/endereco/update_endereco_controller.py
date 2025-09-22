from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.endereco.update_endereco import EnderecoUpdateUseCase as EnderecoUpdateInterface
from src.domain.models.endereco_model import Endereco as EnderecoDomain
class EnderecoUpdateController(ControllerInterface):
    def __init__(self,usecase:EnderecoUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        endereco_id = int(http_request.path_params["id"])
        endereco = EnderecoDomain(**http_request.body) 
        endereco.id = endereco_id
        response = self.usecase.update(
            endereco_id=endereco_id,
            endereco=endereco
        )
        return HTTPResponse(status_code=200,body=response)