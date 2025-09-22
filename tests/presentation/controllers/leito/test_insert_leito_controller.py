from src.presentation.controllers.leito.insert_leito_controller import LeitoInsertController
from tests.data.mock.leito.insert_leito_spy import LeitoInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "numero_leito": "A101",
            "setor_id": 1,
            "tipo": "Enfermaria",
            "status": "disponivel"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = LeitoInsertUsecaseSpy()
    controller = LeitoInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
