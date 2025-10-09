from typing import Optional
from datetime import datetime
class AuthModel:
    def __init__(self,email:str,senha:str,role:Optional[str] = None,createAt:Optional[datetime]=None,updateAt:Optional[datetime]=None,id:Optional[int]=None):
        self.id = id
        self.email = email
        self.senha = senha
        self.role = role
        self.createAt = createAt
        self.updateAt = updateAt