from dataclasses import dataclass
from src.domain.core.entity import Entity
from src.domain.shared.value_objects import Id, Nome

@dataclass
class OrganizacaoProps: 
  cnpj: str
  nome: str
  extensao: str

@dataclass
class State:
  cnpj: str
  nome: Nome
  extensao: str

class Organizacao(Entity[OrganizacaoProps, State]):
  def __init__(self, props: OrganizacaoProps):
    super().__init__(props)
  
  def export(self):
    return OrganizacaoProps(
      self.state.cnpj,
      self.state.nome.export(),
      self.state.extensao
    )
  
  def parse(self, props: OrganizacaoProps) -> State:
    cnpj = props.cnpj
    nome = Nome(props.nome)
    extensao = props.extensao

    return State(cnpj, nome, extensao)
