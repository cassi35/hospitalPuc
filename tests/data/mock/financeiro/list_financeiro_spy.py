from typing import List, Dict

class FinanceiroListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Financeiro",
				"id": 1,
				"attributes": {
					"paciente_id": 1,
					"convenio_id": 1,
					"valor": 150.0,
					"data_emisao": "2025-09-01",
					"data_vencimento": "2025-09-10",
					"status_pagamento": "pendente"
				}
			},
			{
				"type": "Financeiro",
				"id": 2,
				"attributes": {
					"paciente_id": 2,
					"convenio_id": 2,
					"valor": 300.0,
					"data_emisao": "2025-09-05",
					"data_vencimento": "2025-09-15",
					"status_pagamento": "pago"
				}
			}
		]

