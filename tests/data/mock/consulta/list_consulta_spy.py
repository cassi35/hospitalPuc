from typing import List, Dict

class ConsultaListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Consulta",
				"id": 1,
				"attributes": {
					"paciente_id": 1,
					"medico_id": 1,
					"especialidade_id": 1,
					"status": "ativo",
					"data_hora": "2025-09-01",
					"obveservacoes": "Nenhuma"
				}
			},
			{
				"type": "Consulta",
				"id": 2,
				"attributes": {
					"paciente_id": 2,
					"medico_id": 2,
					"especialidade_id": 1,
					"data_hora": "2025-09-02",
					"status": "nao ativo",
					"observacoes": "Nenhuma"
				}
			}
		]

