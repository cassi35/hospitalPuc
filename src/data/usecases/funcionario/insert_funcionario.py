from typing import Dict, List
from datetime import datetime
import re
from src.domain.usecases.funcionario.insert_funcionario import FuncionarioInsertUseCase as FuncionarioInsertInterface
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
from src.domain.models.funcionario_model import Funcionario
from src.errors.types.http_bad_request import HttpBadRequestError

class FuncionarioInsertUseCase(FuncionarioInsertInterface):
    def __init__(self, funcionario_repository: FuncionarioRepositoryInterface, setor_repository: SetorRepositoryInterface):
        self.funcionario_repository = funcionario_repository
        self.setor_repository = setor_repository
    
    def insert(self, funcionario: Funcionario) -> Dict:
        self.__validate_informations(funcionario)
        # create(nome, cpf, cargo, setor_id, telefone, email, data_contratacao)
        self.funcionario_repository.create(
            funcionario.nome,
            funcionario.cpf,
            funcionario.cargo,
            funcionario.setor_id,
            funcionario.telefone,
            funcionario.email,
            funcionario.data_contratacao
        )
        return self.__format_response(funcionario)

    def __validate_informations(self, funcionario: Funcionario) -> None:
        # nome
        if not funcionario.nome or str(funcionario.nome).strip() == "":
            raise HttpBadRequestError("Nome é obrigatório")
        # cpf
        if not funcionario.cpf or not str(funcionario.cpf).isdigit() or len(str(funcionario.cpf)) != 11:
            raise HttpBadRequestError("CPF deve conter 11 dígitos numéricos")
        if self.__cpf_exists(funcionario.cpf):
            raise HttpBadRequestError("CPF já cadastrado")
        # cargo
        if funcionario.cargo not in ['enfermeiro', 'técnico', 'recepcionista']:
            raise HttpBadRequestError("Cargo inválido")
        # setor_id
        if funcionario.setor_id is None or not isinstance(funcionario.setor_id, int) or funcionario.setor_id <= 0:
            raise HttpBadRequestError("setor_id inválido")
        if not self.setor_repository.findById(funcionario.setor_id):
            raise HttpBadRequestError("Setor não encontrado")
        # telefone
        if not funcionario.telefone or not str(funcionario.telefone).isdigit() or len(str(funcionario.telefone)) != 9:
            raise HttpBadRequestError("Telefone deve conter 9 dígitos")
        # email
        if not funcionario.email or not self.__is_valid_email(str(funcionario.email)):
            raise HttpBadRequestError("Email inválido")
        if self.__email_exists(funcionario.email):
            raise HttpBadRequestError("Email já cadastrado")
        # data_contratacao (<= hoje)
        if not funcionario.data_contratacao:
            raise HttpBadRequestError("Data de contratação é obrigatória")
        try:
            data = datetime.strptime(str(funcionario.data_contratacao), '%Y-%m-%d').date()
            if data > datetime.now().date():
                raise HttpBadRequestError("Data de contratação não pode ser futura")
        except ValueError:
            raise HttpBadRequestError("Data de contratação inválida")

    def __cpf_exists(self, cpf: str) -> bool:
        existentes = self.funcionario_repository.findAll()
        return any(getattr(f, "cpf", None) == cpf for f in existentes)

    def __email_exists(self, email: str) -> bool:
        existentes = self.funcionario_repository.findAll()
        return any(str(getattr(f, "email", "")).lower() == str(email).lower() for f in existentes)

    def __is_valid_email(self, email: str) -> bool:
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email) is not None

    def __format_response(self, funcionario: Funcionario) -> Dict:
        return {
            "type": "Funcionario",
            "count": 1,
            "attributes": {
                "nome": funcionario.nome,
                "cpf": funcionario.cpf,
                "cargo": funcionario.cargo,
                "setor_id": funcionario.setor_id,
                "telefone": funcionario.telefone,
                "email": funcionario.email,
                "data_contratacao": str(funcionario.data_contratacao)
            }
        }