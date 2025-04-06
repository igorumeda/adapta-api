from abc import ABC, abstractmethod
from typing import TypeVar, Generic

TProps = TypeVar('TProps')
TState = TypeVar('TState')

class ObjectDomain(ABC, Generic[TProps, TState]):
  def __init__(self, props: TProps):
    self.state = self.parse(props)

  @abstractmethod
  def export(self) -> TProps:
    '''Retornar todas as propriedades como um objeto'''
    pass

  @abstractmethod
  def parse(self, props: TProps) -> TState:
    '''Faça todas as validações das propriedades da entidade'''
    pass