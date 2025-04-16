from dataclasses import dataclass
from src.domain.core.entity import Entity
from src.domain.shared.value_objects import Id, Nome

@dataclass
class DocumentoProps: 
  id: str
  nome: str
  extensao: str

@dataclass
class State:
  id: Id
  nome: Nome
  extensao: str

class Documento(Entity[DocumentoProps, State]):
  def __init__(self, props: DocumentoProps):
    super().__init__(props)
  
  def export(self):
    return DocumentoProps(
      self.state.id.export(),
      self.state.nome.export(),
      self.state.extensao
    )
  
  def parse(self, props: DocumentoProps) -> State:
    id = Id(props.id)
    nome = Nome(props.nome)
    extensao = props.extensao

    return State(id, nome, extensao)
