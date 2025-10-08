from dotenv import load_dotenv
import os
from redis import Redis
class CacheConnectionHandler:
    def __init__(self):
        load_dotenv()
        self.__host = os.getenv('HOST_REDIS')
        self.__port = os.getenv('PORT_REDIS')
        self.__db = os.getenv('DB_REDIS')
        self.__password = os.getenv('PASSWORD_REDIS')
        self.__redis_connection = None
    def  create_redis_connection(self):
        self.__redis_connection = Redis(
            host=self.__host,
            port=self.__port,
            db=self.__db,
            password=self.__password,
            decode_responses=True
        )
        return self.__redis_connection
    def get_connection(self)-> Redis:
        return self.__redis_connection
        