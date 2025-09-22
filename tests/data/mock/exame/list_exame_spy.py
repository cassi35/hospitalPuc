from typing import List, Dict

class ExameListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Exame",
				"id": 1,
				"attributes": {
					"tipo_exame": "Sangue",
					"data_exame": "2025-09-01",
					"paciente_id": 1,
					"medico_id": 1,
					"resultado": "Normal",
					"status": "concluído"
				}
			},
			{
				"type": "Exame",
				"id": 2,
				"attributes": {
					"tipo_exame": "Raio-X",
					"data_exame": "2025-09-02",
					"paciente_id": 2,
					"medico_id": 2,
					"resultado": "Sem fraturas",
					"status": "solicitado"
				}
			}
		]

