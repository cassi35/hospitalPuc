from typing import List, Dict

class PacienteListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Paciente",
				"id": 1,
				"attributes": {
					"nome": "Pedro",
					"cpf": "12345678901",
					"data_nascimento": "1990-01-01",
					"sexo": "m",
					"telefone": "11999999999",
					"contato_emergencia": "11888888888",
					"alergia": "nenhuma",
					"endereco_id": 1,
					"convenio_id": 1
				}
			},
			{
				"type": "Paciente",
				"id": 2,
				"attributes": {
					"nome": "Julia",
					"cpf": "98765432100",
					"data_nascimento": "1985-05-20",
					"sexo": "f",
					"telefone": "21999999999",
					"contato_emergencia": "21888888888",
					"alergia": "poeira",
					"endereco_id": 2,
					"convenio_id": 2
				}
			}
		]

