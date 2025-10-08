from typing import Optional
class UserEmail:
    def __init__(self, email: str, name:  Optional[str] = None,token: Optional[str] = None):
        self.email = email
        self.name = name
        self.token = token