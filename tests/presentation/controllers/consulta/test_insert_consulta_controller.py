from src.presentation.controllers.consulta.insert_consulta_controller import ConsultaInsertController
from tests.data.mock.consulta.insert_consulta_spy import ConsultaInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "data_hora": "2025-09-01",
            "paciente_id": 1,
            "medico_id": 1,
            "especialidade_id": 1,
            "status": "ativo",
            "observacoes": "Retorno"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ConsultaInsertUsecaseSpy()
    controller = ConsultaInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
