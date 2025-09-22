from tests.data.mock.leito.update_leito_spy import LeitoUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.leito.update_leito_controller import LeitoUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "numero_leito": "A101",
            "setor_id": 1,
            "tipo": "Enfermaria",
            "status": "disponivel"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = LeitoUpdateUsecaseSpy()
    controller = LeitoUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
