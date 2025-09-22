from typing import List, Dict

class EspecialidadeListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Especialidade",
				"id": 1,
				"attributes": {
					"nome": "Cardiologia",
					"descricao": "Cuida do coração"
				}
			},
			{
				"type": "Especialidade",
				"id": 2,
				"attributes": {
					"nome": "Ortopedia",
					"descricao": "Cuida dos ossos"
				}
			}
		]

