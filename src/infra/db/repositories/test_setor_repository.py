from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.setor_repository import SetorRepository
from sqlalchemy import text
import pytest

db_connection_handler = BDConnectionHandler()
setor_repository = SetorRepository()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip()
def test_create_setor():
    nome = 'setor A'
    andar = 2
    capacidade = 2
    responsavel = 'cassaino'
    setor_repository.create( nome=nome,andar=andar,capacidade=capacidade,responsavel=responsavel)
    sql = f"select * from setor where nome = '{nome}'"
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['nome'] == nome 
    assert registry['capacidade'] == capacidade
@pytest.mark.skip()
def test_udpate_setor():
    id = 5
    nome = 'setor B'
    andar = 2
    capacidade = 2
    responsavel = 'marcelo'
    setor_repository.update(id=id,nome=nome,andar=andar,capacidade=capacidade,responsavel=responsavel)
    sql = f"select * from setor where id = {id}"
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['nome'] == nome 
    assert registry['capacidade'] == capacidade
    print(registry)
@pytest.mark.skip()
def test_delete_setor():
    id = 5
    delete = setor_repository.delete(id=id)
    sql = f"select * from setor where id = {id}"
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert delete == True
    print(registry) 
@pytest.mark.skip()
def test_findById_setor():
    id = 4
    setor = setor_repository.findById(id=id)
    sql = f"select * from setor where id = {id}"
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['id'] == setor.id
    assert setor is not None
    print(setor.nome)
@pytest.mark.skip()
def test_findAll_setor():
    setores = setor_repository.findAll()
    sql = f"select * from setor;"
    response = connection.execute(text(sql))
    registry = response.all()
    print(setores)