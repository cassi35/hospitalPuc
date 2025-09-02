from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.prescricao_repository import PrescricaoRepository
from sqlalchemy import text
import pytest

db_connection_handler = BDConnectionHandler()
prescricao_repository = PrescricaoRepository()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip()
def test_create_prescricao():
    paciente_id = 1
    medico_id = 1
    data_prescricao = '2025-09-02'
    medicamento_id = 1
    dosagem = 500
    frequencia = 3
    
    prescricao_repository.create(
        paciente_id=paciente_id,
        medico_id=medico_id,
        data_prescricao=data_prescricao,
        medicamento_id=medicamento_id,
        dosagem=dosagem,
        frequencia=frequencia
    )
    
    sql = f'select * from prescricao where paciente_id = {paciente_id} and medico_id = {medico_id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['paciente_id'] == paciente_id
    assert registry['dosagem'] == dosagem
    print(registry)

@pytest.mark.skip()
def test_update_prescricao():
    id = 1
    paciente_id = 1
    medico_id = 2
    data_prescricao = '2025-09-03'
    medicamento_id = 2
    dosagem = 750
    frequencia = 2
    
    prescricao_repository.update(
        id=id,
        paciente_id=paciente_id,
        medico_id=medico_id,
        data_prescricao=data_prescricao,
        medicamento_id=medicamento_id,
        dosagem=dosagem,
        frequencia=frequencia
    )
    
    sql = f'select * from prescricao where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['id'] == id
    assert registry['dosagem'] == dosagem
    print(registry)

@pytest.mark.skip()
def test_delete_prescricao():
    id = 1
    delete = prescricao_repository.delete(id=id)
    assert delete == True
    
    sql = f'select * from prescricao where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry is None

@pytest.mark.skip()
def test_find_by_id_prescricao():
    id = 1
    prescricao = prescricao_repository.findById(id=id)
    assert prescricao is not None
    assert prescricao.id == id
    print(prescricao)

@pytest.mark.skip()
def test_find_all_prescricoes():
    prescricoes = prescricao_repository.findAll()
    assert isinstance(prescricoes, list)
    for prescricao in prescricoes:
        print(prescricao)

@pytest.mark.skip()
def test_find_by_paciente_prescricao():
    paciente_id = 1
    prescricoes = prescricao_repository.findByPaciente(paciente_id=paciente_id)
    assert isinstance(prescricoes, list)
    for prescricao in prescricoes:
        assert prescricao.paciente_id == paciente_id
        print(prescricao)

@pytest.mark.skip()
def test_find_by_medico_prescricao():
    medico_id = 1
    prescricoes = prescricao_repository.findByMedico(medico_id=medico_id)
    assert isinstance(prescricoes, list)
    for prescricao in prescricoes:
        assert prescricao.medico_id == medico_id
        print(prescricao)
