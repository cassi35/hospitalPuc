from typing import Dict, List
from src.domain.usecases.medicamento.list_medicamento import MedicamentoListUseCase as MedicamentoListInterface
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from src.infra.db.entities.medicamento import Medicamento

class MedicamentoListUseCase(MedicamentoListInterface):
    def __init__(self, medicamento_repository: MedicamentoRepositoryInterface):
        self.medicamento_repository = medicamento_repository

    def list(self) -> Dict:
        medicamentos = self.__list_medicamentos()
        return self.__format_response(medicamentos)

    def __list_medicamentos(self) -> List[Medicamento]:
        return self.medicamento_repository.findAll()

    def __format_response(self, medicamentos: List[Medicamento]) -> Dict:
        return {
            "type": "Medicamentos",
            "count": len(medicamentos),
            "attributes": [
                {
                    "id": medicamento.id,
                    "nome": medicamento.nome,
                    "descricao": medicamento.descricao,
                    "fabricante": medicamento.fabricante,
                    "validade": str(medicamento.validade) if medicamento.validade else None,
                    "quantidade_estoque": medicamento.quantidade_estoque
                }
                for medicamento in medicamentos
            ]
        }