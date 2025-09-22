from typing import List, Dict

class InternacaoListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Internacao",
				"id": 1,
				"attributes": {
					"paciente_id": 1,
					"medico_id": 1,
					"leito_id": 1,
					"data_entrada": "2025-09-01",
					"status": "ativa"
				}
			},
			{
				"type": "Internacao",
				"id": 2,
				"attributes": {
					"paciente_id": 2,
					"medico_id": 2,
					"leito_id": 2,
					"data_entrada": "2025-09-05",
					"status": "alta"
				}
			}
		]

