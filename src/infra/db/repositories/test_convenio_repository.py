from src.infra.db.repositories.convenio_repository import ConvenioRepository
from src.infra.db.settings.connection import BDConnectionHandler
from sqlalchemy import text
import pytest
db_connection_handler = BDConnectionHandler()
convenio_repository = ConvenioRepository()
connection = db_connection_handler.get_engine().connect()
@pytest.mark.skip()
def test_insert_convenio():
    nome = 'panvel'
    tipo_plano = 'Individual'
    convenio_repository.insert_convenio(nome=nome,tipo_plano=tipo_plano)
    sql = f"select * from convenio where nome = '{nome}';"
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.nome == nome 
@pytest.mark.skip()
def test_delete_convenio():
    id = 14
    delete = convenio_repository.delete_convenio(id)
    sql = f"select * from convenio where id = {id}"
    response = connection.execute(text(sql))
    print(delete,response)
@pytest.mark.skip()
def test_select_convenio():
    id = 3
    convenio = convenio_repository.select_convenio(id)
    sql = f"select * from convenio where id = {id}"
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    assert registry.id == convenio.id
    assert registry.nome == convenio.nome
    assert registry.tipo_plano == convenio.tipo_plano
@pytest.mark.skip()
def test_update_convenio():
    id = 3
    nome = 'udpate convenio'
    tipo_plano = 'Familiar'
    convenio_repository.udpate_convenio(id=id,nome=nome,tipo_plano=tipo_plano)
    sql = f"select * from convenio where id = {id}"
    response = connection.execute(text(sql))
    registry = response.fetchone()
    print(registry.nome)
    assert registry.id == id
    assert registry.nome == nome 
    assert registry.tipo_plano == tipo_plano
    print(registry) 