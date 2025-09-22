from tests.data.mock.consulta.update_consulta_spy import ConsultaUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.consulta.update_consulta_controller import ConsultaUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
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
    usecase_spy = ConsultaUpdateUsecaseSpy()
    controller = ConsultaUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
