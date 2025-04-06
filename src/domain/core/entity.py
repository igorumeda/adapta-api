from typing import Generic, TypeVar
from src.core import ObjectDomain

TProps = TypeVar('TProps')
TState = TypeVar('TState')

class Entity(Generic[TProps, TState], ObjectDomain[TProps, TState]):
  '''
  Classe base para Entidades do Domínio.
  
  props -> Representa as propriedades da Entidade em formato primitivo (string, int, bool, ...)
  
  state -> Representa o estado da Entidade, com seus valores devidamente validados
  
  Obs.: Implementar decorador @dataclass nos tipos criados
  '''
  pass