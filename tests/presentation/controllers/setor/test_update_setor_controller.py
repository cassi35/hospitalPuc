from tests.data.mock.setor.update_setor_spy import SetorUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.setor.update_setor_controller import SetorUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "nome": "UTI Adulto",
            "andar": 2,
            "capacidade": 10,
            "responsavel": "Carlos"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = SetorUpdateUsecaseSpy()
    controller = SetorUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
