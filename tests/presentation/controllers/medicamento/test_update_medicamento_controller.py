from tests.data.mock.medicamento.update_medicamento_spy import MedicamentoUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.medicamento.update_medicamento_controller import MedicamentoUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "nome": "Dipirona",
            "descricao": "Analgésico",
            "fabricante": "Farmaco SA",
            "validade": "2026-12-31",
            "quantidade_estoque": 50
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = MedicamentoUpdateUsecaseSpy()
    controller = MedicamentoUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
