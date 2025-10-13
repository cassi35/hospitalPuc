from src.infra.services.auth_cahe_service import AuthCacheService
import pytest
from src.infra.services.url_safe_token import URLSafeTokenService
from src.infra.cache.connection import CacheConnectionHandler
cache = CacheConnectionHandler().create_redis_connection()
token = "jwt_blacklist:eyJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAZXhhbXBsZS5jb20ifQ.aOz1fw.WUSumtGX8v-OzO29VvR51npHToM"

@pytest.mark.skip(reason="concluido com sucesso")
def test_blacklist_token():
    data = {"user_id": 1, "email": "test@example.com"}
    url_safe_token = URLSafeTokenService().create_url_safe_token(data=data)
    auth_cache_service = AuthCacheService()
    add_blacklist_token = auth_cache_service.blacklist_token(token=url_safe_token,ttl=3600)
    assert add_blacklist_token == True
@pytest.mark.skip(reason="concluido com sucesso")
def test_is_token_blacklisted():
    auth_cache_service = AuthCacheService()
    is_token = auth_cache_service.is_token_blacklisted(token)
    assert is_token == True
    print(cache.exists(token) != '0')
@pytest.mark.skip(reason="concluido com sucesso")
def test_store_temp_token():
    auth_cache_service = AuthCacheService()
    data = {"user_id": 1, "email": "test@example.com"}
    url_safe_token = URLSafeTokenService().create_url_safe_token(data=data)
    key = f"reset_password:{url_safe_token}"
    store_temp = auth_cache_service.store_temp_token(
        key=key,
        token=url_safe_token
    )
    assert store_temp == True
@pytest.mark.skip(reason="concluido com sucesso")
def test_get_temp_token():
    auth_cache_service = AuthCacheService()
    key = "reset_password:eyJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAZXhhbXBsZS5jb20ifQ.aOz5YQ.Yr4h31dAGiseQC2efIdLGa7R4Pc"
    temp_token = auth_cache_service.get_temp_token(key=key)
    print(temp_token)
    print(cache.get(key))
def test_delete_temp_token():
    auth_cache_service = AuthCacheService()
    key = "jwt_blacklist:eyJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAZXhhbXBsZS5jb20ifQ.aOz3yg.Plw3DUpflp0XjyXpgjzz-plzGtA"
    delete = auth_cache_service.delete_temp_token(key=key)
    print(delete)