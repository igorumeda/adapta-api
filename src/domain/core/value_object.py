from typing import Generic, TypeVar
from src.core import ObjectDomain

TProps = TypeVar('TProps')
TState = TypeVar('TState')

class ValueObject(Generic[TProps, TState], ObjectDomain[TProps, TState]):
  pass