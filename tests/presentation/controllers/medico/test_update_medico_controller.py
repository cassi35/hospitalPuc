from tests.data.mock.medico.update_medico_spy import MedicoUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.medico.update_medico_controller import MedicoUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "nome": "Dra Ana",
            "cpf": "98765432100",
            "especialidade_id": 1,
            "telefone": "888888888",
            "email": "ana@exemplo.com",
            "status": "ativo"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = MedicoUpdateUsecaseSpy()
    controller = MedicoUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
