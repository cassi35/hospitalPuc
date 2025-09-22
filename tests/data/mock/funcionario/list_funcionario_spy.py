from typing import List, Dict

class FuncionarioListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Funcionario",
				"id": 1,
				"attributes": {
					"nome": "Carlos Silva",
					"cpf": "12345678901",
					"cargo": "enfermeiro",
					"setor_id": 1,
					"telefone": "123456789",
					"email": "carlos@hospital.com",
					"data_contratacao": "2025-01-10"
				}
			},
			{
				"type": "Funcionario",
				"id": 2,
				"attributes": {
					"nome": "Maria Souza",
					"cpf": "98765432100",
					"cargo": "técnico",
					"setor_id": 2,
					"telefone": "987654321",
					"email": "maria@hospital.com",
					"data_contratacao": "2024-12-01"
				}
			}
		]

