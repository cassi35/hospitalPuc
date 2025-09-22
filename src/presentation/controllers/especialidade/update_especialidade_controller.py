from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.especialidade.update_especialidade import EspecialidadeUpdateUseCase as EspecialidadeUpdateInterface
from src.domain.models.especialidade_model import Especialidade as EspecialidadeDomain
class EspecialidadeUpdateController(ControllerInterface):
    def __init__(self,usecase:EspecialidadeUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        especialidade_id = int(http_request.path_params["id"])
        especialidade = EspecialidadeDomain(**http_request.body) 
        especialidade.id = especialidade_id
        response = self.usecase.update(
            especialidade_id=especialidade_id,
            especialidade=especialidade
        )
        return HTTPResponse(status_code=200,body=response)
