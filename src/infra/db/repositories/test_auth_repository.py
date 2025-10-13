from src.infra.db.settings.connection import BDConnectionHandler
from src.infra.db.repositories.auth_repository import AuthRepository
from sqlalchemy import text
import pytest
from datetime import datetime
db_connection_handler = BDConnectionHandler()
auth_repository = AuthRepository()
connection = db_connection_handler.get_engine().connect()
@pytest.mark.skip(reason="teste realizado com sucesso")
def test_create_user():
    user_data  = {
    "email": "testedas@gmail.com",
    "nome": "Testess",
    "senha": "hashed_password",
    "role": "Paciente"
    }
    auth_repository.create_user(user_data=user_data)
    sql = f"select * from Auth_user where email = '{user_data['email']}'"
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['email'] == user_data['email']
@pytest.mark.skip(reason="teste realizado com sucesso")

def test_get_user_by_email():
    email= "testedas@gmail.com"
    user = auth_repository.get_user_by_email(email=email)
    assert user.email == email
    # ✅ IMPRIMIR os dados específicos
    print(f"ID: {user.id}")
    print(f"Email: {user.email}")
    # print(f"Nome: {user.nome}")
    print(f"Role: {user.role}")
    print(f"Is Verified: {user.is_verified}")
    print(f"Created At: {user.createAt}")
    print(f"Updated At: {user.updateAt}")
@pytest.mark.skip(reason="teste realizado com sucesso")
def test_get_user_by_id():
    user_id = 5
    user = auth_repository.get_user_by_id(user_id=user_id)
    assert user.id == user_id
    # ✅ IMPRIMIR os dados específicos
    print(f"ID: {user.id}")
    print(f"Email: {user.email}")
    print(f"Role: {user.role}")
    print(f"Is Verified: {user.is_verified}")
    print(f"Created At: {user.createAt}")
    print(f"Updated At: {user.updateAt}")
def test_update_user():
    user_id = 5
    update_data = {
        "email":"testedas@gmail.com",
        "nome": "cassiano",
        "senha": "new_hashed_password",
        "role": "Medico",
        "is_verified": True,
    }
    auth_repository.update_user(user_id=user_id, update_data=update_data)
    sql = f"select * from Auth_user where id = {user_id}"
    response = connection.execute(text(sql))
    registry = response.mappings().fetchone()
    assert registry['nome'] == update_data['nome']
    print(registry)