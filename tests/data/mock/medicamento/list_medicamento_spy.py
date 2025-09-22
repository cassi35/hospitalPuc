from typing import List, Dict

class MedicamentoListUsecaseSpy:
	def __init__(self):
		self.list_call_count = 0
		self.list_was_called = False
        
	def list(self) -> List[Dict]:
		self.list_call_count += 1
		self.list_was_called = True
        
		return [
			{
				"type": "Medicamento",
				"id": 1,
				"attributes": {
					"nome": "Paracetamol",
					"descricao": "Analgésico",
					"fabricante": "Lab ABC",
					"validade": "2025-12-31",
					"quantidade_estoque": 100
				}
			},
			{
				"type": "Medicamento",
				"id": 2,
				"attributes": {
					"nome": "Ibuprofeno",
					"descricao": "Anti-inflamatório",
					"fabricante": "Lab XYZ",
					"validade": "2026-06-30",
					"quantidade_estoque": 50
				}
			}
		]

