from tests.data.mock.funcionario.update_funcionario_spy import FuncionarioUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.funcionario.update_funcionario_controller import FuncionarioUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "nome": "João Silva",
            "cpf": "12345678901",
            "cargo": "enfermeiro",
            "setor_id": 1,
            "telefone": "999999999",
            "email": "joao@exemplo.com",
            "data_contratacao": "2025-09-01"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = FuncionarioUpdateUsecaseSpy()
    controller = FuncionarioUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
