from fastapi import APIRouter
from src.api.core.mapping_modules import MappingModules
from src.api.controllers.usuarios.usuario_module import UsuarioModule

def modules() -> list[APIRouter]:
    return MappingModules(
        modules=[
            UsuarioModule()
        ]
    );
