from passlib.context import CryptContext
from src.data.interfaces.password_service_interface import PasswordServiceInterface
class PasswordService(PasswordServiceInterface):
    def __init__(self):
        self.passwd_context = CryptContext(schemes=["bcrypt"])
    def hash_password(self, password: str) -> str:
        return self.passwd_context.hash(password)
    def verify_password(self, password: str, hashed_password: str) -> bool:
        return self.passwd_context.verify(password, hashed_password)