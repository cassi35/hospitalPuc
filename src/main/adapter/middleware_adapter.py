from fastapi import Request, status, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.errors.types.InvalidToken import InvalidToken
from src.errors.types.AcessTokenRequired import AcessTokenRequired
from src.errors.types.RefreshTokenRequired import RefreshTokenRequired

class AccessTokenMiddleware(HTTPBearer):
    def __init__(self, access_token_usecase, auto_error=True):
        super().__init__(auto_error=auto_error)
        self.access_token_usecase = access_token_usecase  # ✅ SÓ access token usecase

    async def __call__(self, request: Request) -> dict:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        token = credentials.credentials 
        try:
            # ✅ CHAMA o método verify_access do usecase
            token_data = self.access_token_usecase.verify_access(token)
        except (InvalidToken, AcessTokenRequired) as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        return token_data

class RefreshTokenMiddleware(HTTPBearer):
    def __init__(self, refresh_token_usecase, auto_error=True):
        super().__init__(auto_error=auto_error)
        self.refresh_token_usecase = refresh_token_usecase  # ✅ SÓ refresh token usecase

    async def __call__(self, request: Request) -> dict:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        token = credentials.credentials 
        try:
            # ✅ CHAMA o método verify_refresh do usecase
            token_data = self.refresh_token_usecase.verify_refresh(token)
        except (InvalidToken, RefreshTokenRequired) as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        return token_data