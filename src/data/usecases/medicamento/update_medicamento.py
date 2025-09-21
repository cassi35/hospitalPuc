from typing import Dict
from src.domain.usecases.medicamento.update_medicamento import MedicamentoUpdateUseCase as MedicamentoInsertInterface
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from src.infra.db.entities.medicamento import Medicamento
from src.errors.types.http_bad_request import HttpBadRequestError
from datetime import datetime
import re

class MedicamentoUpdateUseCase(MedicamentoInsertInterface):
    def __init__(self, medicamento_repository: MedicamentoRepositoryInterface):
        self.medicamento_repository = medicamento_repository

    def update(self, medicamento_id: int, medicamento: Medicamento) -> Dict:
        self.__exists_medicamento(id=medicamento_id)
        self.__validate_informations(medicamento=medicamento)
        self.__update_medicamento(medicamento=medicamento)
        return self.__format_response(medicamento)
    def __exists_medicamento(self,id:int) -> None:
        if id < 0 or not isinstance(id,int):
            raise HttpBadRequestError("ID inválido")
        exists = self.medicamento_repository.findById(id=id)
        if not exists:
            raise HttpBadRequestError("Medicamento não encontrado")
    def __validate_informations(self, medicamento: Medicamento) -> None:
        # Validar nome
        if not medicamento.nome or medicamento.nome.strip() == "" or medicamento.nome.isalpha() == False:
            raise HttpBadRequestError("Nome do medicamento é obrigatório")
        if len(medicamento.nome) > 30:
            raise HttpBadRequestError("Nome do medicamento deve ter no máximo 30 caracteres")
        
        # Verificar se nome é único
        existing_medicamento = self.medicamento_repository.findByNome( nome=medicamento.nome)
        
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

    def __update_medicamento(self, medicamento: Medicamento) -> None:
        self.medicamento_repository.update(
            nome=medicamento.nome,
            descricao=medicamento.descricao,
            fabricante=medicamento.fabricante,
            validade=medicamento.validade,
            quantidade_estoque=medicamento.quantidade_estoque,
            id=medicamento.id
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