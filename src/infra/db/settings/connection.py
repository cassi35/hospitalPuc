from sqlalchemy import create_engine 
import os 
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

class BDConnectionHandler:
    def __init__(self):
        # Carrega as variáveis do arquivo .env
        load_dotenv()
        
        # Obtém as variáveis de ambiente
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')
        
        self._connection_string = "{}://{}:{}@{}:{}/{}".format(
            "mysql+pymysql", db_user, db_password, db_host, db_port, db_name
        )
        
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