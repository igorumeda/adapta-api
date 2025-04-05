from abc import ABC, abstractmethod
from typing import Any
from fastapi import APIRouter

class Controller(ABC):
    __router__: APIRouter

    def parseInput(self):
        """
        (Opcional) Método que obtém os parâmetros passados via body.
        Pode ser sobrescrito por controllers que precisarem.
        """
        pass

    def parseParams(self):
        """
        (Opcional) Método que obtém os parâmetros passados via URL.
        Pode ser sobrescrito por controllers que precisarem.
        """
        pass

    def parseQuery(self):
        """
        (Opcional) Método que obtém os parâmetros passados via query string.
        Pode ser sobrescrito por controllers que precisarem.
        """
        pass

    @abstractmethod
    def handle(self) -> Any:
        """
        (Obrigatório) Método principal que executa a lógica do controller.
        Deve ser implementado em todas as subclasses.
        """
        pass
