import pytest
from datetime import datetime
from src.infra.services.jwt_service import JWTService
def test_create_and_decode_token():
    jwt_service = JWTService()
    user_data = {"user_id": 123, "role": "admin"}
    token = jwt_service.create_access_token(user_data=user_data)
    decoded = jwt_service.decode_token(token=token)
    print(f"Token: {token}")
    print(f"Decoded: {decoded}")