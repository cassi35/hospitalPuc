from src.presentation.controllers.prescricao.insert_prescricao_controller import PrescricaoInsertController
from tests.data.mock.prescricao.insert_prescricao_spy import PrescricaoInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "paciente_id": 1,
            "medico_id": 1,
            "data_prescricao": "2025-09-01",
            "medicamento_id": 1,
            "dosagem": 1,
            "frequencia": 8
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = PrescricaoInsertUsecaseSpy()
    controller = PrescricaoInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
