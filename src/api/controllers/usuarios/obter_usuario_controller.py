from src.api.application.usuarios.obter_usuarios_service import ObterUsuariosService
from src.api.core.decorator_factory import get
from src.api.core.controller import Controller

@get("/usuarios", tags=["Usuários"])
class ObterUsuarioController(Controller):
    def __init__(self):
        self.service = ObterUsuariosService()

    def handle(self):
        return self.service.handle()
