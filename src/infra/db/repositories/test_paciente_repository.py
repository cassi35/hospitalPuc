from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.infra.db.settings.connection import BDConnectionHandler
from sqlalchemy import text
import pytest
def test_insert_paciente():

    paciente_repository = PacienteRepository()
    nome = 'teste'
    cpf = '12345678903'
    data_nascimento = '1990-01-01'
    sexo = 'm'
    telefone = '12345678903'
    alergia = 'nenhuma'
    contato_emergencia = '12345678903'
    endereco_id = 13
    convenio_id = 1
    paciente_repository.insert_paciente(
        nome=nome,
        cpf=cpf,
        data_nascimento=data_nascimento,
        sexo=sexo,
        telefone=telefone,
        alergia=alergia,
        contato_emergencia=contato_emergencia,
        endereco_id=endereco_id,
        convenio_id=convenio_id
    )
    db_connection_handler = BDConnectionHandler()
    connection = db_connection_handler.get_engine().connect()
    sql = f"""
    select * from Paciente where cpf = '{cpf}';
    """ 
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    assert registry.nome == nome
    assert registry.cpf == cpf
    connection.commit()
    print(registry)