from typing import Dict
from src.domain.usecases.medicamento.insert_medicamento import MedicamentoInsertUseCase as MedicamentoInsertInterface
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from src.infra.db.entities.medicamento import Medicamento
from src.errors.types.http_bad_request import HttpBadRequestError
from datetime import datetime
import re
class MedicamentoInsertUseCase(MedicamentoInsertInterface):
    def __init__(self, medicamento_repository: MedicamentoRepositoryInterface):
        self.medicamento_repository = medicamento_repository

    def insert(self, medicamento: Medicamento) -> Dict:
        self.__validate_informations(medicamento)
        self.__insert_medicamento(medicamento)
        return self.__format_response(medicamento)

    def __validate_informations(self, medicamento: Medicamento) -> None:
        # Validar nome
        if not medicamento.nome or medicamento.nome.strip() == "" or medicamento.nome.isalpha() == False:
            raise HttpBadRequestError("Nome do medicamento é obrigatório")
        if len(medicamento.nome) > 30:
            raise HttpBadRequestError("Nome do medicamento deve ter no máximo 30 caracteres")
        
        # Verificar se nome é único
        existing_medicamento = self.medicamento_repository.findByNome(medicamento.nome)
        if existing_medicamento:
            raise HttpBadRequestError("Já existe um medicamento com este nome")

        # Validar descrição (opcional, mas se informada deve ter no máximo 30 chars)
        if medicamento.descricao and len(medicamento.descricao) > 30:
            raise HttpBadRequestError("Descrição deve ter no máximo 30 caracteres")

        # Validar validade
        if not medicamento.validade:
            raise HttpBadRequestError("Data de validade é obrigatória")
        
        try:
            validade_date = datetime.strptime(str(medicamento.validade), '%Y-%m-%d').date()
            today = datetime.now().date()
            if validade_date < today:
                raise HttpBadRequestError("Data de validade deve ser maior ou igual à data atual")
        except ValueError:
            raise HttpBadRequestError("Data de validade inválida")

        # Validar quantidade_estoque
        if medicamento.quantidade_estoque is None:
            raise HttpBadRequestError("Quantidade em estoque é obrigatória")
        if not isinstance(medicamento.quantidade_estoque, int) or medicamento.quantidade_estoque < 0:
            raise HttpBadRequestError("Quantidade em estoque deve ser um número inteiro maior ou igual a 0")

    def __insert_medicamento(self, medicamento: Medicamento) -> None:
        self.medicamento_repository.create(
            nome=medicamento.nome,
            descricao=medicamento.descricao,
            fabricante=medicamento.fabricante,
            validade=medicamento.validade,
            quantidade_estoque=medicamento.quantidade_estoque
        )

    def __format_response(self, medicamento: Medicamento) -> Dict:
        return {
            "type": "Medicamento",
            "count": 1,
            "attributes": {
                "nome": medicamento.nome,
                "descricao": medicamento.descricao,
                "fabricante": medicamento.fabricante,
                "validade": str(medicamento.validade),
                "quantidade_estoque": medicamento.quantidade_estoque
            }
        }