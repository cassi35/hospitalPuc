from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.setor.insert_setor import SetorInsertUseCase as SetorInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.setor_model import Setor as SetorDomain
class SetorInsertController(ControllerInterface):
    def __init__(self,usecase:SetorInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        setor = SetorDomain(**http_request.body)
        response = self.usecase.insert(
            setor=setor
        )
        return HTTPResponse(status_code=200,body=response)
