from typing import TypeVar
from src.core import ObjectDomain

TProps = TypeVar('TProps')
TState = TypeVar('TState')

class ValueObject[TProps, TState](ObjectDomain[TProps, TState]):
  def __init__(self, props: TProps):
    super().__init__(props)