from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.medicamento_repository import MedicamentoRepository
from sqlalchemy import text
import pytest

db_connection_handler = BDConnectionHandler()
medicamento_repository = MedicamentoRepository()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip()
def test_create_medicamento():
    nome = 'Paracetamol'
    principio_ativo = 'Paracetamol'
    dosagem = '500mg'
    forma_farmaceutica = 'comprimido'
    fabricante = 'Laboratório ABC'
    
    medicamento_repository.create(
        nome=nome,
        principio_ativo=principio_ativo,
        dosagem=dosagem,
        forma_farmaceutica=forma_farmaceutica,
        fabricante=fabricante
    )
    
    sql = f'select * from medicamento where nome = "{nome}" and fabricante = "{fabricante}"'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['nome'] == nome
    assert registry['dosagem'] == dosagem
    print(registry)

@pytest.mark.skip()
def test_update_medicamento():
    id = 1
    nome = 'Ibuprofeno'
    principio_ativo = 'Ibuprofeno'
    dosagem = '400mg'
    forma_farmaceutica = 'comprimido'
    fabricante = 'Laboratório XYZ'
    
    medicamento_repository.update(
        id=id,
        nome=nome,
        principio_ativo=principio_ativo,
        dosagem=dosagem,
        forma_farmaceutica=forma_farmaceutica,
        fabricante=fabricante
    )
    
    sql = f'select * from medicamento where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['id'] == id
    assert registry['nome'] == nome
    print(registry)

@pytest.mark.skip()
def test_delete_medicamento():
    id = 1
    delete = medicamento_repository.delete(id=id)
    assert delete == True
    
    sql = f'select * from medicamento where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry is None

@pytest.mark.skip()
def test_find_by_id_medicamento():
    id = 1
    medicamento = medicamento_repository.findById(id=id)
    assert medicamento is not None
    assert medicamento.id == id
    print(medicamento)

@pytest.mark.skip()
def test_find_all_medicamentos():
    medicamentos = medicamento_repository.findAll()
    assert isinstance(medicamentos, list)
    for medicamento in medicamentos:
        print(medicamento)

@pytest.mark.skip()
def test_find_by_nome_medicamento():
    nome = 'Paracetamol'
    medicamentos = medicamento_repository.findByNome(nome=nome)
    assert isinstance(medicamentos, list)
    for medicamento in medicamentos:
        assert nome in medicamento.nome
        print(medicamento)

@pytest.mark.skip()
def test_find_by_principio_ativo_medicamento():
    principio_ativo = 'Paracetamol'
    medicamentos = medicamento_repository.findByPrincipioAtivo(principio_ativo=principio_ativo)
    assert isinstance(medicamentos, list)
    for medicamento in medicamentos:
        assert principio_ativo in medicamento.principio_ativo
        print(medicamento)
