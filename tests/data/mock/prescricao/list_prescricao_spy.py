from typing import List, Dict

class PrescricaoListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False

	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True

		return [
			{
				"type": "Prescricao",
				"id": 1,
				"attributes": {
					"paciente_id": 1,
					"medico_id": 1,
					"data_prescricao": "2024-01-10",
					"medicamento_id": 1,
					"dosagem": "500mg",
					"frequencia": "8/8h"
				}
			},
			{
				"type": "Prescricao",
				"id": 2,
				"attributes": {
					"paciente_id": 2,
					"medico_id": 2,
					"data_prescricao": "2024-02-15",
					"medicamento_id": 2,
					"dosagem": "1 comprimido",
					"frequencia": "12/12h"
				}
			}
		]

