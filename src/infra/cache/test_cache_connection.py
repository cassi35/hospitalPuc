from .connection import CacheConnectionHandler
import pytest
def test_create_redis_connection():
    cache_connection_handler = CacheConnectionHandler()
    redis_conn = cache_connection_handler.create_redis_connection()
    key = 'test_key'
    value = 'value'
    redis_conn.set(key,value)
    get = redis_conn.get(key)
    assert get == value
    assert redis_conn is not None
