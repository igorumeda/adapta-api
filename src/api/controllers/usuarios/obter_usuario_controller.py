from fastapi import Request
from src.api.application.usuarios.obter_usuarios_service import ObterUsuariosService
from src.api.core.decorator_factory import get
from src.api.core.controller import Controller

@get("/usuarios/{cpf}", tags=["Usuários"])
class ObterUsuarioController(Controller):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.service = ObterUsuariosService()

    async def handle(self):
        cpf = self.rawParams["cpf"]
        return self.service.handle(cpf)
