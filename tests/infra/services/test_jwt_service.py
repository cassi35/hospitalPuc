from src.infra.services.jwt_service import JWTService
import pytest
jwt_service = JWTService()
@pytest.mark.skip(reason="teste com sucesso")
def test_create_access_token():
        user_data = {"user_id": 1, "username": "testuser"}
        token = jwt_service.create_access_token(user_data=user_data)
        print(token)
def test_decode_token():
        decode = jwt_service.decode_token(
                token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2RhdGEiOnsidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0ZXN0dXNlciJ9LCJleHAiOjE3NjAzOTI1MzIsImp0aSI6ImU4ZDBkZjEwLWI1NTUtNDNkNi1iMGJjLWI1NDRjYzUwZTY2MSIsInJlZnJlc2giOmZhbHNlfQ.TKc-xuv19KrKUSg9ZmQMM7QaRLqE2k8nWLV_9XPWF8I"
        )
        print(decode)
        assert decode["user_data"]["user_id"] == 1