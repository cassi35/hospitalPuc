from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.medicamento.update_medicamento import MedicamentoUpdateUseCase as MedicamentoUpdateInterface
from src.domain.models.medicamento_model import Medicamento as MedicamentoDomain
class MedicamentoUpdateController(ControllerInterface):
    def __init__(self,usecase:MedicamentoUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        medicamento_id = int(http_request.path_params["id"])
        medicamento = MedicamentoDomain(**http_request.body) 
        medicamento.id = medicamento_id
        response = self.usecase.update(
            medicamento_id=medicamento_id,
            medicamento=medicamento
        )
        return HTTPResponse(status_code=200,body=response)
