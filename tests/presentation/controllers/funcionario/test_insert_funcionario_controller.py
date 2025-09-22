from src.presentation.controllers.funcionario.insert_funcionario_controller import FuncionarioInsertController
from tests.data.mock.funcionario.insert_funcionario_spy import FuncionarioInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
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
    usecase_spy = FuncionarioInsertUsecaseSpy()
    controller = FuncionarioInsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
