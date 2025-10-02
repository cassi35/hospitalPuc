from typing import Optional
class UserEmail:
    def __init__(self, email: str, name: str,token: Optional[str]):
        self.email = email
        self.name = name
        self.token = token