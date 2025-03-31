from fastapi import APIRouter
from typing import Callable, Type
from src.api.core.controller import Controller

def _create_method_decorator(http_method: str) -> Callable[[str], Callable[[Type[Controller]], Type[Controller]]]:
    def decorator(path: str) -> Callable[[Type[Controller]], Type[Controller]]:
        def wrapper(cls: Type[Controller]) -> Type[Controller]:
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
