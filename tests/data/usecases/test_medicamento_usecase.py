from tests.infra.repositories.medicamento_repository_spy import MedicamentoRepositorySpy
from src.data.usecases.medicamento.insert_medicamento import MedicamentoInsertUseCase
from src.data.usecases.medicamento.delete_medicamento import MedicamentoDeleteUseCase
from src.data.usecases.medicamento.update_medicamento import MedicamentoUpdateUseCase
from src.data.usecases.medicamento.list_medicamento import MedicamentoListUseCase
from src.domain.models.medicamento_model import Medicamento as MedicamentoDomain 
import pytest
medicamento_repository_spy = MedicamentoRepositorySpy()
@pytest.mark.skip(reason='concluido teste')
def test_medicamento_insert():
    medicamento_insert_usecase = MedicamentoInsertUseCase(medicamento_repository=medicamento_repository_spy)
    nome = 'Paracetamol'
    descricao = 'Analgésico e antipirético'
    fabricante = 'Laboratório ABC'
    validade = '2025-12-31'
    quantidade_estoque = 2
    medicamento = MedicamentoDomain(
        nome=nome,
        descricao=descricao,
        fabricante=fabricante,
        validade=validade,
        quantidade_estoque=quantidade_estoque,
        id=2
    )
    response = medicamento_insert_usecase.insert(
        medicamento=medicamento 
    )
    print(response)
def test_update_medicamento(): 
    medicamento_update_usecase = MedicamentoUpdateUseCase(
        medicamento_repository=medicamento_repository_spy
    )
    nome = 'Paracetamol'
    descricao = 'Analgésico e antipirético'
    fabricante = 'Laboratório ABC'
    validade = '2025-12-31'
    quantidade_estoque = 2
    medicamento = MedicamentoDomain(
        nome=nome,
        descricao=descricao,
        fabricante=fabricante,
        validade=validade,
        quantidade_estoque=quantidade_estoque,
        id=2
    )
    response = medicamento_update_usecase.update(
        medicamento=medicamento,
        medicamento_id=2
    )
    print(response)