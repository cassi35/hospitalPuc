from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.especialidade.delete_especialidade import EspecialidadeDeleteUseCase as EspecialidadeDeleteInterface
class EspecialidadeDeleteController(ControllerInterface): 
    def __init__(self,usecase:EspecialidadeDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        especialidade_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            especialidade_id=especialidade_id
        )
        return HTTPResponse(status_code=200,body=response)
