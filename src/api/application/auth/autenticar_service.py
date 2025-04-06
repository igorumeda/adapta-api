from typing import Any, cast
from api.infra.adapters.json.usuario_adapter import UsuarioAdapter
from src.api.core.application_service import ApplicationService
from fastapi import Cookie, HTTPException, status
from jwt import ExpiredSignatureError, InvalidTokenError
from api.core.provider import TokenPayload, TokenProvider

class AutenticarService(ApplicationService):
    def __init__(self):
        self.usuarioAdapter = UsuarioAdapter()
        self.tokenProvider = TokenProvider()

    def handle(self, accessToken: str = Cookie(None)) -> object:
        if not accessToken:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Você não está autenticado"
            )
        
        payload: TokenPayload = TokenProvider.TokenDecode(accessToken)
        
        usuario = self.usuarioAdapter.obter()
        if not usuario or not usuario.validar_senha(senha):
            raise Unauthorized("Credenciais inválidas")

        accessToken = self.token_provider.gerar_access_token(cpf)
        refresh_token = self.token_provider.gerar_refresh_token(cpf)

        return {
            "access_token": accessToken,
            "refresh_token": refresh_token
        }
        




class AuthController(Controller):
  def handle(self, access_token: str = Cookie(None)):
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

