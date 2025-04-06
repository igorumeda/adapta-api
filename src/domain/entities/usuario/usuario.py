from dataclasses import dataclass
from src.domain.core.entity import Entity
from src.shared.exceptions.domain_exception import DomainException

@dataclass
class UsuarioProps:
  id: str
  nome: str
  cpf: str
  email: str
  senha: str
  
@dataclass
class State:
  id: str
  nome: str
  cpf: str
  email: str
  senha: str
  
class Usuario(Entity[UsuarioProps, State]):
  def __init__(self, props: UsuarioProps):
    super().__init__(props)
  
  def export(self):
    return UsuarioProps(
      self.state.id,
      self.state.nome,
      self.state.cpf,
      self.state.email,
      self.state.senha,
    )
    
  def parse(self, props: UsuarioProps) -> State:
    if props.cpf.__len__() != 11:
      raise DomainException("CPF inválido")
    
    return State(
      props.id,
      props.nome,
      props.cpf,
      props.email,
      props.senha,
    )