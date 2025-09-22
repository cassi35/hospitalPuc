from src.presentation.controllers.setor.insert_setor_controller import SetorInsertController
from tests.data.mock.setor.insert_setor_spy import SetorInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "nome": "UTI Adulto",
            "andar": 2,
            "capacidade": 10,
            "responsavel": "Carlos"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = SetorInsertUsecaseSpy()
    controller = SetorInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
