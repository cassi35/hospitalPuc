from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.especialidade_repository import EspecialidadeRepository
from sqlalchemy import text
import pytest
db_connection_handler = BDConnectionHandler()
especidade_repository = EspecialidadeRepository()
connection = db_connection_handler.get_engine().connect()
@pytest.mark.skip()
def test_create_especialidade():
    nome = 'Cardiologia'
    descricao = 'Especialidade médica que se dedica ao estudo, diagnóstico e tratamento das doenças do coração e do sistema circulatório.'
    especidade_repository.create(nome=nome,descricao=descricao)
    sql = f"select * from especialidade where descricao = '{descricao}';"
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.nome == nome 
    assert registry.descricao == descricao
    print(registry)
@pytest.mark.skip()
def test_update_especialidade():
    id = 1
    nome = 'Cardiologia Update'
    descricao = 'Especialidade médica que se dedica ao estudo, diagnóstico e tratamento das doenças do coração e do sistema circulatório. Update'
    especidade_repository.update(id=id,nome=nome,descricao=descricao)
    sql = f"select * from especialidade where id = {id}"
    response = connection.execute(text(sql))
    registry = response.fetchone()
    print(registry.nome)
    assert registry.id == id
    assert registry.nome == nome 
    assert registry.descricao == descricao
    print(registry)
@pytest.mark.skip()
def test_delete_especialidade():
    id = 12
    delete = especidade_repository.delete(id)
    sql = f"select * from especialidade where id = {id}"
    response = connection.execute(text(sql))
    print(delete,response)
@pytest.mark.skip()
def test_findById_especialidade():
    id = 2
    especialidade = especidade_repository.findById(id)
    sql = f"select * from especialidade where id = {id}"
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    assert registry.id == especialidade.id
    assert registry.nome == especialidade.nome
    assert registry.descricao == especialidade.descricao
    print(especialidade.nome)