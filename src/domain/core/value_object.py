from typing import Generic, TypeVar
from src.domain.core.object_domain import ObjectDomain

TProps = TypeVar('TProps')
TState = TypeVar('TState')

class ValueObject(Generic[TProps, TState], ObjectDomain[TProps, TState]):
  '''
  Classe base para Value Objects do Domínio.
  
  props -> Representa as propriedades da Entidade em formato primitivo (string, int, bool, ...)
  
  state -> Representa o estado da Entidade, com seus valores devidamente validados
  
  Obs.: Implementar decorador @dataclass nos tipos criados
  '''
  def __init__(self, props: TProps):
    super().__init__(props)