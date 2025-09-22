from src.presentation.controllers.internacao.insert_internacao_controller import InternacaoInsertController
from tests.data.mock.internacao.insert_internacao_spy import InternacaoInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "paciente_id": 1,
            "medico_id": 1,
            "leito_id": 1,
            "data_entrada": "2025-09-01",
            "status": "em andamento"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = InternacaoInsertUsecaseSpy()
    controller = InternacaoInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
