import jwt
from typing import Any
from datetime import datetime, timedelta
from core.settings import Settings
from pydantic import BaseModel

class TokenPayload(BaseModel):
    sub: str
    exp: int  

class TokenProvider:
    @staticmethod
    def AcessTokenGenerate(cpf: str) -> str:
        exp: int = int((datetime.now() + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp())
        payload: TokenPayload = TokenPayload(sub=cpf, exp=exp)
        return jwt.encode(payload, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM) # type: ignore
    
    @staticmethod
    def RefreshTokenGenerate(cpf: str) -> str:
        exp: int = int((datetime.now() + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp())
        payload: TokenPayload = TokenPayload(sub=cpf, exp=exp)
        return jwt.encode(payload, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM) # type: ignore

    @staticmethod
    def TokenDecode(token: str) -> TokenPayload:
        tokenDecoded: dict[str, Any] = jwt.decode(token, Settings.SECRET_KEY, algorithms=[Settings.ALGORITHM]) # type: ignore
        return TokenPayload(**tokenDecoded)