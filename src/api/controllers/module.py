from fastapi import APIRouter
from src.api.core.mapping_modules import MappingModules
from src.api.controllers.usuarios._usuario_module import UsuarioModule

def routes() -> list[APIRouter]:
    return MappingModules([
        UsuarioModule()
    ])
