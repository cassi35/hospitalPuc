from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.medicamento.delete_medicamento import MedicamentoDeleteUseCase as MedicamentoDeleteInterface
class MedicamentoDeleteController(ControllerInterface): 
    def __init__(self,usecase:MedicamentoDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        medicamento_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            medicamento_id=medicamento_id
        )
        return HTTPResponse(status_code=200,body=response)
