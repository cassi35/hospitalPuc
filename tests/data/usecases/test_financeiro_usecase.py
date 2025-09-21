from tests.infra.repositories.financeiro_repository_spy import FinanceiroRepositorySpy
from tests.infra.repositories.paciente_repository_spy import PacienteRepositorySpy
from tests.infra.repositories.convenio_repository_spy import ConvenioRepositorySpy
from src.data.usecases.financeiro.insert_financeiro import FinanceiroInsertUseCase
from src.data.usecases.financeiro.delete_financeiro import FinanceiroDeleteUseCase
from src.data.usecases.financeiro.update_financeiro import FinanceiroUpdateUseCase
from src.data.usecases.financeiro.list_financeiro import FinanceiroListUseCase
from src.domain.models.financeiro_model import Financeiro as FinanceiroDomain
import pytest

financeiro_repository_spy = FinanceiroRepositorySpy()
paciente_repository_spy = PacienteRepositorySpy()
convenio_repository_spy = ConvenioRepositorySpy()

@pytest.mark.skip(reason="concluido")
def test_insert_financeiro():
    financeiro_insert_usecase = FinanceiroInsertUseCase(
        financeiro_repository=financeiro_repository_spy,
        paciente_repository=paciente_repository_spy,
        convenio_repository=convenio_repository_spy
    )
    financeiro = FinanceiroDomain(
        id=1,
        paciente_id=1,
        convenio_id=1,
        valor=150.0,
        data_emisao="2023-01-01",
        data_vencimento="2024-01-10",
        status_pagamento="pendente"
    )
    response = financeiro_insert_usecase.insert(financeiro=financeiro)
    print(response)

@pytest.mark.skip(reason="concluido")
def test_delete_financeiro():
    financeiro_delete_usecase = FinanceiroDeleteUseCase(
        financeiro_repository=financeiro_repository_spy
    )
    response = financeiro_delete_usecase.delete(1)
    print(response)

@pytest.mark.skip(reason="concluido")
def test_update_financeiro():
    financeiro_update_usecase = FinanceiroUpdateUseCase(
        financeiro_repository=financeiro_repository_spy,
        paciente_repository=paciente_repository_spy,
        convenio_repository=convenio_repository_spy
    )
    financeiro = FinanceiroDomain(
        id=1,
        paciente_id=1,
        convenio_id=1,
        valor=200.0,
        data_emisao="2024-01-01",
        data_vencimento="2024-01-15",
        status_pagamento="pago"
    )
    response = financeiro_update_usecase.update(financeiro_id=1, financeiro=financeiro)
    print(response)

@pytest.mark.skip(reason="concluido")
def test_list_financeiro():
    financeiro_list_usecase = FinanceiroListUseCase(
        financeiro_repository=financeiro_repository_spy
    )
    response = financeiro_list_usecase.list()
    print(response)