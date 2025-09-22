from typing import List, Dict

class LeitoListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Leito",
				"id": 1,
				"attributes": {
					"numero_leito": "A101",
					"setor_id": 1,
					"tipo": "UTI",
					"status": "alta"
				}
			},
			{
				"type": "Leito",
				"id": 2,
				"attributes": {
					"numero_leito": "B202",
					"setor_id": 2,
					"tipo": "Enfermaria",
					"status": "obito"
				}
			}
		]

