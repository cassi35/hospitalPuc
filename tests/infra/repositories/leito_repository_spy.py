from typing import List
from src.domain.models.leito_model import Leito as LeitoDomain
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface
class LeitoRepositorySpy(LeitoRepositoryInterface):
    def __init__(self):
        self.create_leito_attributes = {}
        self.create_leito_call_count = 0

        self.update_leito_attributes = {}
        self.update_leito_call_count = 0

        self.delete_leito_attributes = {}
        self.delete_leito_call_count = 0

        self.findAll_leito_attributes = {}
        self.findAll_leito_call_count = 0

        self.findById_leito_attributes = {}
        self.findById_leito_call_count = 0

        self.findByStatus_leito_attributes = {}
        self.findByStatus_leito_call_count = 0

    def create(self, numero_leito: int, setor_id: int, tipo: str, status: str) -> None:
        self.create_leito_attributes = {
            "numero_leito": numero_leito,
            "setor_id": setor_id,
            "tipo": tipo,
            "status": status
        }
        self.create_leito_call_count += 1

    def update(self, id:int, numero_leito: int, setor_id: int, tipo: str, status: str) -> None:
        self.update_leito_attributes = {
            "id": id,
            "numero_leito": numero_leito,
            "setor_id": setor_id,
            "tipo": tipo,
            "status": status
        }
        self.update_leito_call_count += 1
    def delete(self, id)-> bool:
        self.delete_leito_attributes = {"id":id}
        self.delete_leito_call_count +=1
        return True
    def findById(self, id:int)-> LeitoDomain:
        self.findById_leito_attributes = {"id":id}
        self.findById_leito_call_count +=1
        leito = LeitoDomain(
            id=id,
            numero_leito=101,
            setor_id=1,
            tipo="Tipo Teste",
            status="Disponível"
        )
        return leito
    def findAll(self)-> List[LeitoDomain]:
        self.findAll_leito_attributes = {}
        self.findAll_leito_call_count +=1
        leito1 = LeitoDomain(
            id=1,
            numero_leito=101,
            setor_id=1,
            tipo="Tipo A",
            status="Disponível"
        )
        leito2 = LeitoDomain(
            id=2,
            numero_leito=102,
            setor_id=1,
            tipo="Tipo B",
            status="Ocupado"
        )
        return [leito1, leito2]
    def findByStatus(self, status:str)->List[LeitoDomain]:
        self.findByStatus_leito_attributes = {"status":status}
        self.findByStatus_leito_call_count +=1
        leito1 = LeitoDomain(
            id=1,
            numero_leito=101,
            setor_id=1,
            tipo="Tipo A",
            status=status
        )
        leito2 = LeitoDomain(
            id=2,
            numero_leito=102,
            setor_id=1,
            tipo="Tipo B",
            status=status
        )
        return [leito1, leito2]