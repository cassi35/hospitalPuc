from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.funcionario_repository import FuncionarioRepository
from sqlalchemy import text
import pytest

db_connection_handler = BDConnectionHandler()
funcionario_repository = FuncionarioRepository()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip()
def test_create_funcionario():
    nome = 'Carlos Silva'
    cargo = 'Enfermeiro'
    setor_id = 1
    cpf = '12345678901'
    telefone = '11987654321'
    email = 'carlos@hospital.com'
    funcionario_repository.create(
        nome=nome,
        cargo=cargo,
        setor_id=setor_id,
        cpf=cpf,
        telefone=telefone,
        email=email,
        data_contratacao="2023-10-01"
    )
    
    sql = f'select * from funcionario where cpf = "{cpf}" and email = "{email}"'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['nome'] == nome
    assert registry['cargo'] == cargo
    print(registry)

@pytest.mark.skip()
def test_update_funcionario():
    id = 1
    nome = 'Carlos Santos'
    cargo = 'Enfermeiro Chefe'
    setor_id = 2
    cpf = '12345678901'
    telefone = '11987654322'
    email = 'carlos.santos@hospital.com'
    
    funcionario_repository.update(
        id=id,
        nome=nome,
        cargo=cargo,
        setor_id=setor_id,
        cpf=cpf,
        telefone=telefone,
        email=email,
        data_contratacao="2023-10-01"
    )
    
    sql = f'select * from funcionario where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['id'] == id
    assert registry['cargo'] == cargo
    print(registry)

@pytest.mark.skip()
def test_delete_funcionario():
    id = 1
    delete = funcionario_repository.delete(id=id)
    assert delete == True
    
    sql = f'select * from funcionario where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry is None

@pytest.mark.skip()
def test_find_by_id_funcionario():
    id = 1
    funcionario = funcionario_repository.findById(id=id)
    assert funcionario is not None
    assert funcionario.id == id
    print(funcionario)

@pytest.mark.skip()
def test_find_all_funcionarios():
    funcionarios = funcionario_repository.findAll()
    assert isinstance(funcionarios, list)
    for funcionario in funcionarios:
        print(funcionario)

@pytest.mark.skip()
def test_find_by_nome_funcionario():
    nome = 'Carlos'
    funcionarios = funcionario_repository.findByNome(nome=nome)
    assert isinstance(funcionarios, list)
    for funcionario in funcionarios:
        assert nome in funcionario.nome
        print(funcionario)

@pytest.mark.skip()
def test_find_by_cargo_funcionario():
    cargo = 'Enfermeiro'
    funcionarios = funcionario_repository.findByCargo(cargo=cargo)
    assert isinstance(funcionarios, list)
    for funcionario in funcionarios:
        assert cargo in funcionario.cargo
        print(funcionario)

@pytest.mark.skip()
def test_find_by_setor_funcionario():
    setor_id = 1
    funcionarios = funcionario_repository.findBySetor(setor_id=setor_id)
    assert isinstance(funcionarios, list)
    for funcionario in funcionarios:
        assert funcionario.setor_id == setor_id
        print(funcionario)
