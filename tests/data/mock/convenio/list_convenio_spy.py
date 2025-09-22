from typing import List, Dict

class ConvenioListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Convenio",
				"id": 1,
				"attributes": {
					"nome": "Plano A",
					"tipo_plano": "Individual"
				}
			},
			{
				"type": "Convenio",
				"id": 2,
				"attributes": {
					"nome": "Plano B",
					"tipo_plano": "Familiar"
				}
			}
		]

