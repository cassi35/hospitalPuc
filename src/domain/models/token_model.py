class TokenModel:
    def __init__(self, user_data: dict, jti: str, exp: int, refresh: bool = False):
        self.user_data = user_data
        self.jti = jti
        self.exp = exp
        self.refresh = refresh