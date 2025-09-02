from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.financeiro_repository import FinanceiroRepository
from sqlalchemy import text
import pytest

db_connection_handler = BDConnectionHandler()
financeiro_repository = FinanceiroRepository()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip()
def test_create_financeiro():
    paciente_id = 1
    valor = 1500.50
    data_vencimento = '2025-10-15'
    data_pagamento = '2025-10-10'
    status = 'pago'
    descricao = 'Consulta cardiologia'
    
    financeiro_repository.create(
        paciente_id=paciente_id,
        valor=valor,
        data_vencimento=data_vencimento,
        data_pagamento=data_pagamento,
        status=status,
        descricao=descricao
    )
    
    sql = f'select * from financeiro where paciente_id = {paciente_id} and descricao = "{descricao}"'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['paciente_id'] == paciente_id
    assert registry['valor'] == valor
    print(registry)

@pytest.mark.skip()
def test_update_financeiro():
    id = 1
    paciente_id = 1
    valor = 2000.75
    data_vencimento = '2025-11-15'
    data_pagamento = '2025-11-10'
    status = 'pago'
    descricao = 'Exame atualizado'
    
    financeiro_repository.update(
        id=id,
        paciente_id=paciente_id,
        valor=valor,
        data_vencimento=data_vencimento,
        data_pagamento=data_pagamento,
        status=status,
        descricao=descricao
    )
    
    sql = f'select * from financeiro where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['id'] == id
    assert registry['valor'] == valor
    print(registry)

@pytest.mark.skip()
def test_delete_financeiro():
    id = 1
    delete = financeiro_repository.delete(id=id)
    assert delete == True
    
    sql = f'select * from financeiro where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry is None

@pytest.mark.skip()
def test_find_by_id_financeiro():
    id = 1
    financeiro = financeiro_repository.findById(id=id)
    assert financeiro is not None
    assert financeiro.id == id
    print(financeiro)

@pytest.mark.skip()
def test_find_all_financeiros():
    financeiros = financeiro_repository.findAll()
    assert isinstance(financeiros, list)
    for financeiro in financeiros:
        print(financeiro)

@pytest.mark.skip()
def test_find_by_paciente_financeiro():
    paciente_id = 1
    financeiros = financeiro_repository.findByPaciente(paciente_id=paciente_id)
    assert isinstance(financeiros, list)
    for financeiro in financeiros:
        assert financeiro.paciente_id == paciente_id
        print(financeiro)

@pytest.mark.skip()
def test_find_by_status_financeiro():
    status = 'pago'
    financeiros = financeiro_repository.findByStatus(status=status)
    assert isinstance(financeiros, list)
    for financeiro in financeiros:
        assert financeiro.status == status
        print(financeiro)
