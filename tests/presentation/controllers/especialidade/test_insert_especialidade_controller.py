from src.presentation.controllers.especialidade.insert_especialidade_controller import EspecialidadeInsertController
from tests.data.mock.especialidade.insert_especialidade_spy import EspecialidadeInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "nome": "Cardiologia",
            "descricao": "Coração e vasos"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = EspecialidadeInsertUsecaseSpy()
    controller = EspecialidadeInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
