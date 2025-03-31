from typing import Callable, TypeVar, Any, cast

F = TypeVar('F', bound=Callable[..., Any])

def Serializable(id: str) -> Callable[[F], F]:
    def Serialize(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)
        return cast(F, wrapper)
    return Serialize
