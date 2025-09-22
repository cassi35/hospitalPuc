from src.presentation.controllers.financeiro.insert_financeiro_controller import FinanceiroInsertController
from tests.data.mock.financeiro.insert_financeiro_spy import FinanceiroInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "paciente_id": 1,
            "convenio_id": 1,
            "valor": 100.0,
            "data_emisao": "2025-09-01",
            "data_vencimento": "2025-09-10",
            "status_pagamento": "pendente"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = FinanceiroInsertUsecaseSpy()
    controller = FinanceiroInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
