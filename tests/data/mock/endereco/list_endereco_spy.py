from typing import List, Dict

class EnderecoListUsecaseSpy:
    def __init__(self):
        self.list_call_count = 0
        self.list_was_called = False
        
    def list(self) -> List[Dict]:
        self.list_call_count += 1
        self.list_was_called = True
        
        return [
            {
                "type": "Endereco",
                "id": 1,
                "attributes": {
                    "rua": "Rua Teste",
                    "bairro": "Bairro Teste", 
                    "cidade": "Cidade Teste",
                    "estado": "Estado Teste",
                    "cep": "12345678"
                }
            },
            {
                "type": "Endereco", 
                "id": 2,
                "attributes": {
                    "rua": "Outra Rua",
                    "bairro": "Outro Bairro",
                    "cidade": "Outra Cidade", 
                    "estado": "Outro Estado",
                    "cep": "87654321"
                }
            }
        ]