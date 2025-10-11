from src.infra.services.auth_cahe_service import AuthCacheService
import pytest
from src.infra.services.url_safe_token import URLSafeTokenService
token = "jwt_blacklist:eyJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAZXhhbXBsZS5jb20ifQ.aOkVww.t1Ipz75kiqxNWBlJZeA2Qp2ekYk"
@pytest.mark.skip(reason="concluido com sucesso")
def test_blacklist_token():
    data = {"user_id": 1, "email": "test@example.com"}
    url_safe_token = URLSafeTokenService().create_url_safe_token(data=data)
    auth_cache_service = AuthCacheService()
    add_blacklist_token = auth_cache_service.blacklist_token(token=url_safe_token,ttl=3600)
    assert add_blacklist_token == True
def test_is_token_blacklisted():
    auth_cache_service = AuthCacheService()
    is_token = auth_cache_service.is_token_blacklisted(token)
    print(is_token)
    assert is_token == True