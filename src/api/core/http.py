from fastapi import APIRouter
from typing import Callable, Type, TypeVar
from src.api.core.controller import Controller

T = TypeVar("T", bound=Controller)

def _create_method_decorator(http_method: str) -> Callable[[str], Callable[[Type[T]], Type[T]]]:
    def decorator(path: str) -> Callable[[Type[T]], Type[T]]:
        def wrapper(cls: Type[T]) -> Type[T]:
            instance = cls()
            router = APIRouter()
            route_func = getattr(router, http_method.lower())
            route_func(path)(instance.handle)
            instance.__router__ = router
            return cls 
        return wrapper
    return decorator

get = _create_method_decorator("get")
post = _create_method_decorator("post")
put = _create_method_decorator("put")
delete = _create_method_decorator("delete")
