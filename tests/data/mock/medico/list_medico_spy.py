from typing import List, Dict

class MedicoListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Medico",
				"id": 1,
				"attributes": {
					"nome": "Dr. João",
					"cpf": "12345678901",
					"especialidade_id": 1,
					"telefone": "123456789",
					"email": "joao@hospital.com",
					"status": "ativo"
				}
			},
			{
				"type": "Medico",
				"id": 2,
				"attributes": {
					"nome": "Dra. Ana",
					"cpf": "98765432100",
					"especialidade_id": 2,
					"telefone": "987654321",
					"email": "ana@hospital.com",
					"status": "nao ativo"
				}
			}
		]

