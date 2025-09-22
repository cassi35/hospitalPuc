from tests.data.mock.exame.update_exame_spy import ExameUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.exame.update_exame_controller import ExameUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "tipo_exame": "Hemograma",
            "data_exame": "2025-09-01",
            "paciente_id": 1,
            "medico_id": 1,
            "resultado": "Normal",
            "status": "solicitado"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ExameUpdateUsecaseSpy()
    controller = ExameUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
