from abc import ABC
from typing import Optional

class BaseException(ABC, Exception):
  code: int
  message: str
  
  def __init__(self, code: str, message: Optional[str], *args):
    super().__init__(*args)
    self.code = code
    self.message = message