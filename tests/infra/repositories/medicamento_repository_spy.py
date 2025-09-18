from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from src.domain.models.medicamento_model import Medicamento as MedicamentoDomain 
from typing import List
class MedicamentoRepositorySpy(MedicamentoRepositoryInterface):
    def __init__(self):
        self.create_medicamento_attributes = {}
        self.create_medicamento_call_count = 0

        self.update_medicamento_attributes = {}
        self.update_medicamento_call_count = 0

        self.delete_medicamento_attributes = {}
        self.delete_medicamento_call_count = 0

        self.findById_medicamento_attributes = {}
        self.findById_medicamento_call_count = 0

        self.findAll_medicamento_attributes = {}
        self.findAll_medicamento_call_count = 0

        self.findByNome_medicamento_attributes = {}
        self.findByNome_medicamento_call_count = 0

        self.delete_medicamento_return = True
    def create(self, nome: str, descricao: str, fabricante: str, validade: str, quantidade_estoque: int) -> None:
        self.create_medicamento_attributes = {
            "nome": nome,
            "descricao": descricao,
            "fabricante": fabricante,
            "validade": validade,
            "quantidade_estoque": quantidade_estoque
        }
        self.create_medicamento_call_count += 1
    def update(self, id: int, nome: str, descricao: str, fabricante: str, validade: str, quantidade_estoque: int) -> None:
        self.update_medicamento_attributes = {
            "id": id,
            "nome": nome,
            "descricao": descricao,
            "fabricante": fabricante,
            "validade": validade,
            "quantidade_estoque": quantidade_estoque
        }
        self.update_medicamento_call_count += 1
    def delete(self, id: int) -> bool:
        self.delete_medicamento_attributes = {"id":id}
        self.delete_medicamento_call_count +=1
        return self.delete_medicamento_return
    def findById(self, id: int) -> MedicamentoDomain:
        self.findById_medicamento_attributes = {"id":id}
        self.findById_medicamento_call_count += 1
        medicamento = MedicamentoDomain(
            id=id,
            nome="Medicamento Teste",
            descricao="Descricao Teste",
            fabricante="Fabricante Teste",
            validade="2023-10-10",
            quantidade_estoque=10
        )
        return medicamento
    def findAll(self) -> List[MedicamentoDomain]:
        self.findAll_medicamento_attributes = {}
        self.findAll_medicamento_call_count +=1
        medicamento1 = MedicamentoDomain(
            id=1,
            nome="Medicamento A",
            descricao="Descricao A",
            fabricante="Fabricante A",
            validade="2023-10-10",
            quantidade_estoque=10
        )
        medicamento2 = MedicamentoDomain(
            id=2,
            nome="Medicamento B",
            descricao="Descricao B",
            fabricante="Fabricante B",
            validade="2024-10-10",
            quantidade_estoque=20
        )
        return [medicamento1, medicamento2]
    def findByNome(self, nome: str) -> MedicamentoDomain:
        self.findByNome_medicamento_attributes = {"nome":nome}
        self.findByNome_medicamento_call_count +=1
        medicamento = MedicamentoDomain(
            id=1,
            nome=nome,
            descricao="Descricao Teste",
            fabricante="Fabricante Teste",
            validade="2023-10-10",
            quantidade_estoque=10
        )
        return medicamento