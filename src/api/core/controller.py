from abc import ABC, abstractmethod
from typing import Any, Type, TypeVar
from fastapi import APIRouter, Request
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class Controller(ABC):
    __router__: APIRouter
    
    def __init__(self, request: Request) -> None:
        self.__request = request
        self.rawParams = self.__request.path_params
        '''Dicionário que obtém os parâmetros enviados na URL.'''
        self.rawQuery = self.__request.query_params
        '''Dicionário que obtém os paramêtros enviados via QueryString.'''
        
    async def rawInput(self, model: Type[T]) -> Any:
        '''
        Obtém o json enviado no body.
        
        Recebe o parâmetro 'model' que representa um objeto com o formato do JSON recebido. 
        Este objeto deve ser uma classe que herda de BaseModel.
        '''
        data = await self.__request.json()
        return model(**data)
        

    @abstractmethod
    def handle(self) -> Any:
        """
        (Obrigatório) Método principal que executa a lógica do controller.
        
        Deve ser implementado em todas os controllers.
        """
        pass
