from src.api.controllers.usuarios.obter_usuario_controller import ObterUsuarioController
from src.api.core.controller import Controller

def UsuarioModule() -> list[type[Controller]]:
    return [
        ObterUsuarioController
    ]