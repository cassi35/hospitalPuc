from tests.data.mock.internacao.update_internacao_spy import InternacaoUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.internacao.update_internacao_controller import InternacaoUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "paciente_id": 1,
            "medico_id": 1,
            "leito_id": 1,
            "data_entrada": "2025-09-01",
            "status": "em andamento"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = InternacaoUpdateUsecaseSpy()
    controller = InternacaoUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
