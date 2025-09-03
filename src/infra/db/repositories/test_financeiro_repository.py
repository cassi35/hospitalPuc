from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.financeiro_repository import FinanceiroRepository
from sqlalchemy import text
import pytest

db_connection_handler = BDConnectionHandler()
financeiro_repository = FinanceiroRepository()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip()
def test_create_financeiro():
    paciente_id = 10
    valor = 1500.50
    convenio_id = 2
    data_vencimento = '2025-10-15'
    data_emisao = '2025-10-10'
    status_pagamento = 'pago'
    financeiro_repository.create(
        convenio_id=convenio_id,
        data_emisao=data_emisao,
        data_vencimento=data_vencimento,
        paciente_id=paciente_id,
        status_pagamento=status_pagamento,
        valor=valor
    )
    
    sql = f'select * from financeiro where paciente_id = {paciente_id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['paciente_id'] == paciente_id
    assert registry['valor'] == valor
    print(registry)

@pytest.mark.skip()
def test_update_financeiro():
    id = 1
    paciente_id = 10
    valor = 1500.50
    convenio_id = 2
    data_vencimento = '2025-10-15'
    data_emisao = '2025-10-10'
    status_pagamento = 'Pendente'
    financeiro_repository.update(
        id=id,
        convenio_id=convenio_id,
        data_emisao=data_emisao,
        data_vencimento=data_vencimento,
        paciente_id=paciente_id,
        status_pagamento=status_pagamento,
        valor=valor
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
    id = 2
    financeiro = financeiro_repository.findById(id=id)
    assert financeiro != None
    assert financeiro.id == id
    print(financeiro)

@pytest.mark.skip()
def test_find_all_financeiros():
    financeiros = financeiro_repository.findAll()
    assert isinstance(financeiros, list)
    for financeiro in financeiros:
        print(financeiro)

