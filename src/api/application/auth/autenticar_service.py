from api.infra.adapters.json.usuario_adapter import UsuarioAdapter
from src.api.core.application_service import ApplicationService
from fastapi import Cookie, HTTPException, status
from api.core.provider import TokenProvider

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
        
        payload = TokenProvider.TokenDecode(accessToken)
        
        usuario = self.usuarioAdapter.obterPor(payload.sub)
        if not usuario:
            raise Exception("Credenciais inválidas")

        return {
            "message": "Você está autenticado!"
        }      