from src.presentation.controllers.exame.insert_exame_controller import ExameInsertController
from tests.data.mock.exame.insert_exame_spy import ExameInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
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
    usecase_spy = ExameInsertUsecaseSpy()
    controller = ExameInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
