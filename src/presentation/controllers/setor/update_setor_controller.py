from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.setor.update_setor import SetorUpdateUseCase as SetorUpdateInterface
from src.domain.models.setor_model import Setor as SetorDomain
class SetorUpdateController(ControllerInterface):
    def __init__(self,usecase:SetorUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        setor_id = int(http_request.path_params["id"])
        setor = SetorDomain(**http_request.body) 
        setor.id = setor_id
        response = self.usecase.update(
            setor_id=setor_id,
            setor=setor
        )
        return HTTPResponse(status_code=200,body=response)
