from dataclasses import dataclass
from src.core import Entity
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
  def export(self):
    return DocumentoProps(
      id = self.state.id.export(),
      nome = self.state.nome.export(),
      extensao = self.state.extensao
    )
  
  def parse(self, props: DocumentoProps) -> State:
    id = Id(props.id)
    nome = Nome(props.nome)
    extensao = props.extensao

    return State(id, nome, extensao)
