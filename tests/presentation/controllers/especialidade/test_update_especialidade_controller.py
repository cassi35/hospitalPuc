from tests.data.mock.especialidade.update_especialidade_spy import EspecialidadeUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.especialidade.update_especialidade_controller import EspecialidadeUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "nome": "Cardiologia",
            "descricao": "Coração e vasos"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = EspecialidadeUpdateUsecaseSpy()
    controller = EspecialidadeUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
