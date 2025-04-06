from domain.core.value_object import ValueObject
from src.shared.exceptions.domain_exception import DomainException
from src.shared.utils.nano_id import NanoId

class Id(ValueObject[str, str]):
  def __init__(self, props: str):
    super().__init__(props)

  def export(self) -> str:
    return self.state
  
  def parse(self, props: str) -> str:
    if not (NanoId.validate(props)): 
      raise DomainException("Id inválido")
    return props