from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.exame_repository import ExameRepository
from sqlalchemy import text
from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
import pytest

db_connection_handler = BDConnectionHandler()
exame_repository = ExameRepository()
connection = db_connection_handler.get_engine().connect()
paciente_repository = PacienteRepository()
medico_repository = MedicoRepository()
@pytest.mark.skip()
def test_create_exame():
    tipo_exame = 'Exame de sangue'
    data_exame = '2025-09-02'
    paciente_id = 10
    medico_id = 2
    resultado = 'Normal'
    status = 'concluído'
    
    exame_repository.create(
        tipo_exame=tipo_exame,
        data_exame=data_exame,
        paciente_id=paciente_id,
        medico_id=medico_id,
        resultado=resultado,
        status=status
    )
    
    sql = f'select * from Exame where paciente_id = {paciente_id} and tipo_exame = "{tipo_exame}"'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['paciente_id'] == paciente_id
    assert registry['status'] == status
    print(registry)

@pytest.mark.skip()
def test_update_exame():
    id = 5
    tipo_exame = 'Exame de urina'
    data_exame = '2025-09-03'
    paciente_id = 10
    medico_id = 2
    resultado = 'Alterado'
    status = 'em andamento'
    
    exame_repository.update(
        id=id,
        tipo_exame=tipo_exame,
        data_exame=data_exame,
        paciente_id=paciente_id,
        medico_id=medico_id,
        resultado=resultado,
        status=status
    )
    
    sql = f'select * from Exame where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['id'] == id
    assert registry['status'] == status
    print(registry)

@pytest.mark.skip()
def test_delete_exame():
    id = 5
    delete = exame_repository.delete(id=id)
    assert delete == True
    
    sql = f'select * from Exame where id = {id}'
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry is None

@pytest.mark.skip()
def test_find_by_id_exame():
    id = 2
    exame = exame_repository.findById(id=id)
    assert exame is not None
    assert exame.id == id
    print(exame)

@pytest.mark.skip()
def test_find_all_exames():
    exames = exame_repository.findAll()
    assert isinstance(exames, list)
    for exame in exames:
        paciente = paciente_repository.select_paciente(exame.paciente_id)
        medico = medico_repository.findById(exame.medico_id)
        print(f"paciente {paciente.nome} medico {medico.nome}")

