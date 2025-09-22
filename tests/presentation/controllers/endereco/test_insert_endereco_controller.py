from src.presentation.controllers.endereco.insert_endereco_controller import EnderecoInsertController
from tests.data.mock.endereco.insert_endereco_spy import EnderecoInsertUsecaseSpy
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            'rua': 'Rua XV de Novembro',
            'bairro': 'Centro',
            'cidade': 'Curitiba',
            'estado': 'PR',
            'cep': '80020000'
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = EnderecoInsertUsecaseSpy()
    endereco_insert_controller = EnderecoInsertController(usecase_spy)
    response = endereco_insert_controller.handle(http_request_mock)
    print(response)