from sqlalchemy import create_engine 
from src.config import Config
from sqlalchemy.orm import sessionmaker
class BDConnectionHandler:
    def __init__(self):
        db_user = Config.DB_USER
        db_password = Config.DB_PASSWORD
        db_host = Config.DB_HOST
        db_port = Config.DB_PORT
        db_name = Config.DB_NAME

        self._connection_string ="mysql+pymysql://root:root@hospitalDB/HospitalSaoLucas"
        # Inicializa o engine
        self.__engine = self.__create_database_engine()
    
    def __create_database_engine(self):
        engine = create_engine(self._connection_string, echo=True)
        return engine
    
    def create_tables(self):
        from infra.db.settings.base import Base
        Base.metadata.create_all(self.__engine)
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection")
        self.session.close()