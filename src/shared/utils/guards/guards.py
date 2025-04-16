from typing import Callable, Any, List, Optional, Tuple

class Guards:
    def __init__(self):
        self.__validators: List[Tuple[Callable[[str, Any], Optional[str]], str, Any]] = []
        self.__errors: List[str] = []

    def add(self, validator: Callable[[str, Any], Optional[str]], field_name: str, value: Any) -> None:
        self.__validators.append((validator, field_name, value))

    def hasError(self) -> bool:
        self.__errors.clear()
        for func, name, value in self.__validators:
            message = func(name, value)
            if message:
                self.__errors.append(message)
        return len(self.__errors) > 0

    def getErrors(self) -> List[str]:
        return self.__errors
