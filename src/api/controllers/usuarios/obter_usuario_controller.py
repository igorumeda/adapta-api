from fastapi import APIRouter
from src.api.core.controller import Controller
from src.api.core.http import get

@get("/usuarios")
class ObterUsuarioController(Controller):
    __router__ = APIRouter()

    def handle(self) -> object:
        return {"id": 1, "nome": "Fulano"}
