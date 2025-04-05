import jwt
from typing import Any
from datetime import datetime, timedelta
from core.settings import Settings
from pydantic import BaseModel
from fastapi import Cookie, HTTPException, status
from jwt import ExpiredSignatureError, InvalidTokenError

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
      
    @staticmethod
    def Validate(access_token: str = Cookie(None)):
      if not access_token:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Você não está autenticado"
        )

      try:
          payload: TokenPayload = TokenProvider().TokenDecode(access_token)
          
      except ExpiredSignatureError:
          raise HTTPException(status_code=401, detail="Token expirado")
      except InvalidTokenError:
          raise HTTPException(status_code=401, detail="Token inválido")