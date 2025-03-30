from src.core.object_domain import ObjectDomain
from src.shared.exceptions.domain_exception import DomainException
from src.shared.utils.nano_id import NanoId

class Id(ObjectDomain[str, str]):
  def __init__(self, props: str):
    super().__init__(props)

  def export(self) -> str:
    return id
  
  def parse(self, props):
    if not (NanoId.validate(props)): 
      raise DomainException("Id inválido")
    return props