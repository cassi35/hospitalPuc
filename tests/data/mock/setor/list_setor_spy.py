from typing import List, Dict

class SetorListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False

	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True

		return [
			{
				"type": "Setor",
				"id": 1,
				"attributes": {
					"nome": "Emergencia",
					"andar": 1,
					"capacidade": 20,
					"responsavel": "Dra. Ana"
				}
			},
			{
				"type": "Setor",
				"id": 2,
				"attributes": {
					"nome": "UTI",
					"andar": 3,
					"capacidade": 10,
					"responsavel": "Dr. Carlos"
				}
			}
		]

