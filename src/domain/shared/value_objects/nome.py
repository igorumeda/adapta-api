from domain.core.value_object import ValueObject
from src.shared.exceptions import DomainException

class Nome(ValueObject[str, str]):
  def __init__(self, props: str):
    super().__init__(props)

  def export(self):
    return self.state
  
  def parse(self, props: str):
    if not (props.__len__() < 3):
      raise DomainException("Nome inválido")
    return props