from abc import ABC, abstractmethod
from typing import Any


class ApplicationService(ABC):
  @abstractmethod
  def handle(self, *args: Any, **kwargs: Any) -> Any:
    pass