from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.consulta_repository import ConsultaRepository
from sqlalchemy import text
import pytest

db_connection_handler = BDConnectionHandler()
consulta_repository = ConsultaRepository()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip()
def test_create_consulta():
    data_hora = '2025-09-02'
    paciente_id = 10
    medico_id = 1
    especialidade_id = 1
    status = 'ativo'
    observacoes = 'Consulta de rotina'
    
    consulta_repository.create(
        data_hora=data_hora,
        paciente_id=paciente_id,
        medico_id=medico_id,
        especialidade_id=especialidade_id,
        status=status,
        observacoes=observacoes
    )
    
    sql = f'select * from Consulta where paciente_id = {paciente_id} and medico_id = {medico_id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['paciente_id'] == paciente_id
    assert registry['medico_id'] == medico_id
    assert registry['status'] == status
    print(registry)

@pytest.mark.skip()
def test_update_consulta():
    id = 10
    data_hora = '2025-09-03'
    paciente_id = 10
    medico_id = 2
    especialidade_id = 2
    status = 'ativo'
    observacoes = 'Consulta atualizada'
    
    consulta_repository.update(
        id=id,
        data_hora=data_hora,
        paciente_id=paciente_id,
        medico_id=medico_id,
        especialidade_id=especialidade_id,
        status=status,
        observacoes=observacoes
    )
    
    sql = f'select * from Consulta where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['id'] == id
    assert registry['status'] == status
    print(registry)

@pytest.mark.skip()
def test_delete_consulta():
    id = 10
    delete = consulta_repository.delete(id=id)
    assert delete == True
    
    sql = f'select * from Consulta where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry is None

@pytest.mark.skip()
def test_find_by_id_consulta():
    id = 1
    consulta = consulta_repository.findById(id=id)
    assert consulta is not None
    assert consulta.id == id
    print(consulta)

@pytest.mark.skip()
def test_find_all():
    consultas = consulta_repository.findAll()
    assert len(consultas) != 0