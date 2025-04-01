from enum import Enum
from fastapi import APIRouter
from typing import Callable, Literal, Type, TypeVar, Union
from src.api.core.controller import Controller

T = TypeVar("T", bound=Controller)

HttpMethod = Union[Literal["get"], Literal["post"], Literal["put"], Literal["delete"]]

def route(method: HttpMethod):
    def decorator_factory(
        path: str, *, tags: list[str | Enum] = []
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            instance = cls()
            router = APIRouter()
            getattr(router, method)(path, tags=tags)(instance.handle)
            cls.__router__ = router
            return cls
        return decorator
    return decorator_factory

get = route("get")
post = route("post")
put = route("put")
delete = route("delete")