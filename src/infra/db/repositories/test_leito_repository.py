from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.leito_repository import LeitoRepository
from sqlalchemy import text
import pytest

db_connection_handler = BDConnectionHandler()
leito_repository = LeitoRepository()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip()
def test_create_leito():
    numero = 101
    setor_id = 1
    tipo = 'apartamento'
    status = 'disponivel'
    
    leito_repository.create(
        numero=numero,
        setor_id=setor_id,
        tipo=tipo,
        status=status
    )
    
    sql = f'select * from leito where numero = {numero} and setor_id = {setor_id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['numero'] == numero
    assert registry['tipo'] == tipo
    print(registry)

@pytest.mark.skip()
def test_update_leito():
    id = 1
    numero = 102
    setor_id = 2
    tipo = 'enfermaria'
    status = 'ocupado'
    
    leito_repository.update(
        id=id,
        numero=numero,
        setor_id=setor_id,
        tipo=tipo,
        status=status
    )
    
    sql = f'select * from leito where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['id'] == id
    assert registry['status'] == status
    print(registry)

@pytest.mark.skip()
def test_delete_leito():
    id = 1
    delete = leito_repository.delete(id=id)
    assert delete == True
    
    sql = f'select * from leito where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry is None

@pytest.mark.skip()
def test_find_by_id_leito():
    id = 1
    leito = leito_repository.findById(id=id)
    assert leito is not None
    assert leito.id == id
    print(leito)

@pytest.mark.skip()
def test_find_all_leitos():
    leitos = leito_repository.findAll()
    assert isinstance(leitos, list)
    for leito in leitos:
        print(leito)

@pytest.mark.skip()
def test_find_by_setor_leito():
    setor_id = 1
    leitos = leito_repository.findBySetor(setor_id=setor_id)
    assert isinstance(leitos, list)
    for leito in leitos:
        assert leito.setor_id == setor_id
        print(leito)

@pytest.mark.skip()
def test_find_by_status_leito():
    status = 'disponivel'
    leitos = leito_repository.findByStatus(status=status)
    assert isinstance(leitos, list)
    for leito in leitos:
        assert leito.status == status
        print(leito)
