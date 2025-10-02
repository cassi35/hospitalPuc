from typing import List
from src.domain.models.funcionario_model import Funcionario as FuncionarioDomain
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface

class FuncionarioRepositorySpy(FuncionarioRepositoryInterface):
    def __init__(self):
        self.create_funcionario_attributes = {}
        self.create_funcionario_call_count = 0

        self.update_funcionario_attributes = {}
        self.update_funcionario_call_count = 0

        self.delete_funcionario_attributes = {}
        self.delete_funcionario_call_count = 0

        self.findById_funcionario_attributes = {}
        self.findById_funcionario_call_count = 0

        self.findAll_funcionario_call_count = 0

    def create(self, nome: str, cpf: str, cargo: str, setor_id: int, telefone: str, email: str, data_contratacao: str) -> None:
        self.create_funcionario_attributes = {
            "nome": nome,
            "cpf": cpf,
            "cargo": cargo,
            "setor_id": setor_id,
            "telefone": telefone,
            "email": email,
            "data_contratacao": data_contratacao
        }
        self.create_funcionario_call_count += 1

    def update(self, id: int, nome: str, cpf: str, cargo: str, setor_id: int, telefone: str, email: str, data_contratacao: str) -> None:
        self.update_funcionario_attributes = {
            "id": id,
            "nome": nome,
            "cpf": cpf,
            "cargo": cargo,
            "setor_id": setor_id,
            "telefone": telefone,
            "email": email,
            "data_contratacao": data_contratacao
        }
        self.update_funcionario_call_count += 1

    def delete(self, id: int) -> bool:
        self.delete_funcionario_attributes = {"id": id}
        self.delete_funcionario_call_count += 1
        return True

    def findById(self, id: int) -> FuncionarioDomain:
        self.findById_funcionario_attributes = {"id": id}
        self.findById_funcionario_call_count += 1
        # Retorno fake para teste
        return FuncionarioDomain(
            id=id,
            nome="Funcionario Teste",
            cpf="12345678901",
            cargo="enfermeiro",
            setor_id=1,
            telefone="999999999",
            email="teste@teste.com",
            data_contratacao="2024-01-01"
        )

    def findAll(self) -> List[FuncionarioDomain]:
        self.findAll_funcionario_call_count += 1
        funcionario1 = FuncionarioDomain(
            id=1,
            nome="Funcionario 1",
            cpf="12345678901",
            cargo="enfermeiro",
            setor_id=1,
            telefone="999999999",
            email="f1@teste.com",
            data_contratacao="2024-01-01"
        )
        funcionario2 = FuncionarioDomain(
            id=2,
            nome="Funcionario 2",
            cpf="98765432100",
            cargo="técnico",
            setor_id=2,
            telefone="988888888",
            email="f2@teste.com",
            data_contratacao="2024-02-01"
        )
        return [funcionario1, funcionario2]
    def findByEmail(self, email:str)-> FuncionarioDomain:
        funcionario = FuncionarioDomain(
               id=2,
            nome="Funcionario 2",
            cpf="98765432100",
            cargo="técnico",
            setor_id=2,
            telefone="988888888",
            email="sobral@gmail.com",
            data_contratacao="2024-02-01"
        )
        return funcionario