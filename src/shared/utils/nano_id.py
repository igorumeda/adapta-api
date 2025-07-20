import re
from nanoid import generate

class NanoId:
  @staticmethod
  def create() -> str: 
    return generate(size=20)
  
  @staticmethod
  def validate(id: str) -> bool:
    padrao = r'^[a-zA-Z0-9_-]{' + str(20) + r'}$'
    return bool(re.match(padrao, id))
