from tests.data.mock.paciente.update_paciente_spy import PacienteUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.paciente.update_paciente_controller import PacienteUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "nome": "Carlos",
            "cpf": "11122233344",
            "data_nascimento": "1990-01-01",
            "sexo": "m",
            "telefone": "99988877766",
            "contato_emergencia": "99887766554",
            "alergia": "Nenhuma",
            "endereco_id": 1,
            "convenio_id": 1
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = PacienteUpdateUsecaseSpy()
    controller = PacienteUpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
