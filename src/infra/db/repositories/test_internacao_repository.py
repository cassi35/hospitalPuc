from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.internacao_repository import InternacaoRepository
from sqlalchemy import text
import pytest

db_connection_handler = BDConnectionHandler()
internacao_repository = InternacaoRepository()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip()
def test_create_internacao():
    paciente_id = 1
    medico_id = 1
    data_internacao = '2025-09-01'
    data_alta = '2025-09-05'
    leito_id = 1
    motivo = 'Tratamento pneumonia'
    status = 'internado'
    
    internacao_repository.create(
        paciente_id=paciente_id,
        medico_id=medico_id,
        data_internacao=data_internacao,
        data_alta=data_alta,
        leito_id=leito_id,
        motivo=motivo,
        status=status
    )
    
    sql = f'select * from internacao where paciente_id = {paciente_id} and motivo = "{motivo}"'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['paciente_id'] == paciente_id
    assert registry['status'] == status
    print(registry)

@pytest.mark.skip()
def test_update_internacao():
    id = 1
    paciente_id = 1
    medico_id = 2
    data_internacao = '2025-09-02'
    data_alta = '2025-09-07'
    leito_id = 2
    motivo = 'Tratamento atualizado'
    status = 'alta'
    
    internacao_repository.update(
        id=id,
        paciente_id=paciente_id,
        medico_id=medico_id,
        data_internacao=data_internacao,
        data_alta=data_alta,
        leito_id=leito_id,
        motivo=motivo,
        status=status
    )
    
    sql = f'select * from internacao where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['id'] == id
    assert registry['status'] == status
    print(registry)

@pytest.mark.skip()
def test_delete_internacao():
    id = 1
    delete = internacao_repository.delete(id=id)
    assert delete == True
    
    sql = f'select * from internacao where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry is None

@pytest.mark.skip()
def test_find_by_id_internacao():
    id = 1
    internacao = internacao_repository.findById(id=id)
    assert internacao is not None
    assert internacao.id == id
    print(internacao)

@pytest.mark.skip()
def test_find_all_internacoes():
    internacoes = internacao_repository.findAll()
    assert isinstance(internacoes, list)
    for internacao in internacoes:
        print(internacao)

@pytest.mark.skip()
def test_find_by_paciente_internacao():
    paciente_id = 1
    internacoes = internacao_repository.findByPaciente(paciente_id=paciente_id)
    assert isinstance(internacoes, list)
    for internacao in internacoes:
        assert internacao.paciente_id == paciente_id
        print(internacao)

@pytest.mark.skip()
def test_find_by_medico_internacao():
    medico_id = 1
    internacoes = internacao_repository.findByMedico(medico_id=medico_id)
    assert isinstance(internacoes, list)
    for internacao in internacoes:
        assert internacao.medico_id == medico_id
        print(internacao)

@pytest.mark.skip()
def test_find_by_status_internacao():
    status = 'internado'
    internacoes = internacao_repository.findByStatus(status=status)
    assert isinstance(internacoes, list)
    for internacao in internacoes:
        assert internacao.status == status
        print(internacao)
