from enum import Enum
from fastapi import APIRouter, Request
from typing import Callable, Literal, Type, TypeVar, Union
from src.api.core.controller import Controller

T = TypeVar("T", bound=Controller)
HttpMethod = Union[Literal["get"], Literal["post"], Literal["put"], Literal["delete"]]

def route(method: HttpMethod):
    def decorator_factory(
        path: str, *, tags: list[str | Enum] = []
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            router = APIRouter()

            async def endpoint(request: Request):
                controller = cls(request)
                return await controller.handle()

            getattr(router, method)(path, tags=tags)(endpoint)
            cls.__router__ = router
            return cls
        return decorator
    return decorator_factory

get = route("get")
post = route("post")
put = route("put")
delete = route("delete")
