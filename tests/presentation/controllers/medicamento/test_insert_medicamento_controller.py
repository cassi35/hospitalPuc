from src.presentation.controllers.medicamento.insert_medicamento_controller import MedicamentoInsertController
from tests.data.mock.medicamento.insert_medicamento_spy import MedicamentoInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "nome": "Dipirona",
            "descricao": "Analgésico",
            "fabricante": "Farmaco SA",
            "validade": "2026-12-31",
            "quantidade_estoque": 50
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = MedicamentoInsertUsecaseSpy()
    controller = MedicamentoInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
