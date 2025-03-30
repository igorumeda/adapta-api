from src.core import ObjectDomain
from src.shared.exceptions import DomainException

class Nome(ObjectDomain[str, str]):
  def __init__(self, props):
    super().__init__(props)
    self.__props = props

  def export(self):
    return self.__props
  
  def _parse(self, props):
    if not (props):
      raise DomainException("Nome inválido")

    return props