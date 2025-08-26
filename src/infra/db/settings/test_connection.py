from .connection import BDConnectionHandler
import pytest
def test_create_database_engine():
    db_connection_handler = BDConnectionHandler()
    engine = db_connection_handler.get_engine()
    assert engine is not None