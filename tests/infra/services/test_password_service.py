from src.infra.services.password_service import PasswordService
def test_hash_and_verify_password():
    password_service = PasswordService()
    password = "my_secure_password"
    hashed_password = password_service.hash_password(password)
    assert hashed_password != password  # Verifica se a senha foi realmente hasheada
    assert password_service.verify_password(password, hashed_password)  # Verifica se a senha bate com o hash
    assert not password_service.verify_password("wrong_password", hashed_password)  # Verifica se uma senha errada não bate com o hash