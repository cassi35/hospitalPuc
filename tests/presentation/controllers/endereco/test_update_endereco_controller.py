from src.presentation.controllers.endereco.update_endereco_controller import EnderecoUpdateController
from tests.data.mock.endereco.update_endereco_spy import EnderecoUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            'rua': 'Rua XV de Novembro',
            'bairro': 'Centro',
            'cidade': 'Curitiba',
            'estado': 'PR',
            'cep': '80020000'

        }
def test_handler():
    http_request_mock = HttpRequestMock()
    usecase_spy = EnderecoUpdateUsecaseSpy()
    endereco_update_controller = EnderecoUpdateController(
        usecase=usecase_spy
    )
    response = endereco_update_controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None