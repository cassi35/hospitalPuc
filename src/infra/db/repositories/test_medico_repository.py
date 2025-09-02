from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.medico_repository import MedicoRepository
from sqlalchemy import text
import pytest
db_connection_handler = BDConnectionHandler()
medico_repository = MedicoRepository()
connection = db_connection_handler.get_engine().connect()
@pytest.mark.skip()
def test_create_medico():
    nome = 'cassiano'
    cpf = '12345678901'
    especialidade_id = 2
    telefone = '119999993'
    email = 'cassiano@gmail.com'
    status = 'ativo'
    medico_repository.create(
        cpf=cpf,
        email=email,
        especialidade_id=especialidade_id,
        nome=nome,
        telefone=telefone,
        status=status
    )
    sql = f'select * from Medico where cpf = {cpf}'

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    assert registry.nome == nome
    assert registry.telefone == telefone
    print(registry)    
@pytest.mark.skip()
def test_update_medico():
    id = 7
    nome = 'pedro'
    cpf = '12345678901'
    especialidade_id = 2
    telefone = '119999993'
    email = 'cassiano@gmail.com'
    status = 'ativo'
    medico_repository.update(
        id=id,
        cpf=cpf,
        email=email,
        nome=nome,
        especialidade_id=especialidade_id,
        status=status,
        telefone=telefone
        )
    sql = f'select * from Medico where id = {id}'
    response = connection.execute(text(sql))
    registry = response.fetchone()
    assert registry[0] == id
    print(registry)
@pytest.mark.skip()
def test_delete_medico():
    id = 7
    delete = medico_repository.delete(id=id)
    sql = f"select * from Medico where id = {id}"
    response = connection.execute(text(sql))
    print(delete,response)

@pytest.mark.skip()
def test_find_all_medicos():
    medicos = medico_repository.findAll()
    assert isinstance(medicos, list)
    for medico in medicos:
        print(f"{medico.id} {medico.cpf}  {medico.email}")
    # Se quiser garantir que pelo menos um médico existe:
    # assert len(medicos) > 0

@pytest.mark.skip()
def test_find_by_cpf_medico():
    cpf = '98765432100'  # coloque um CPF que exista no banco
    medico = medico_repository.findByCpf(cpf)
    assert medico is not None
    assert medico.cpf == cpf
    print(medico.email,medico.nome)