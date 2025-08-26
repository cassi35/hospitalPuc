from src.infra.db.repositories.endereco_reposotory import EnderecoRepository
from src.infra.db.settings.connection import BDConnectionHandler
from sqlalchemy import text
import pytest
db_connection_handler = BDConnectionHandler()
connection = db_connection_handler.get_engine().connect()
@pytest.mark.skip()
def test_insert_endereco():
    rua = 'Av. Paulista'
    bairro = 'Centro cassiano teste'
    cidade = "porto alegre"
    estado = "RS"
    cep = "80020000"
    endereco_repository = EnderecoRepository()
    endereco_repository.insert_endereco(rua=rua,bairro=bairro,cep=cep,cidade=cidade,estado=estado)
    sql = f"""
select * from Endereco where estado = '{estado}'	;
""" 
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    assert registry.rua == rua
    assert registry.cidade == cidade
    connection.commit()
    print(registry)
def test_select_endereco():
    id = 11
    endereco_repository = EnderecoRepository()
    endereco = endereco_repository.select_endereco(id)
    sql = f"""
    select * from Endereco where id = '{id}'	;
    """ 
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    assert registry.id == id
    connection.commit()
    print(f"nome do bairro{endereco.bairro}")