from fastapi import APIRouter
from src.api.controllers.usuarios.obter_usuario_controller import ObterUsuarioController

def UsuarioModule() -> list[APIRouter]:
    return [
        ObterUsuarioController.__router__
    ]