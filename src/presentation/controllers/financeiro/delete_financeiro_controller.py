from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.financeiro.delete_financeiro import FinanceiroDeleteUseCase as FinanceiroDeleteInterface
class FinanceiroDeleteController(ControllerInterface): 
    def __init__(self,usecase:FinanceiroDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        financeiro_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            financeiro_id=financeiro_id
        )
        return HTTPResponse(status_code=200,body=response)
