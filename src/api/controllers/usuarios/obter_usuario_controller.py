from src.api.core.decorator_factory import get
from src.api.core.controller import Controller

@get("/usuarios", tags=["Usuários"])
class ObterUsuarioController(Controller):
    def handle(self):
        return {"id": "1", "nome": "Fulano"}
