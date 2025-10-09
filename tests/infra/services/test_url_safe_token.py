import pytest
from src.infra.services.url_safe_token import URLSafeTokenService

def test_create_and_decode_url_safe_token():
    service = URLSafeTokenService()
    data = {"email": "test@hospital.com", "user_id": 123}
    token = service.create_url_safe_token(data)
    decoded = service.decode_url_safe_token(token)
    assert decoded["email"] == "test@hospital.com"
    assert decoded["user_id"] == 123

def test_invalid_token_raises_exception():
    service = URLSafeTokenService()
    with pytest.raises(Exception):
        service.decode_url_safe_token("invalid.token.here")