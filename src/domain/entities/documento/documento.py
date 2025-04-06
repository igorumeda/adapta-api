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
  def __init__(self, props: DocumentoProps):
    super().__init__(props)

  def export(self):
    return DocumentoProps(
      id = self.state.id.export(),
      nome = self.state.nome.export(),
      extensao = self.state.extensao
    )
  
  def parse(self, props: DocumentoProps) -> State:
    id = Id(props.id).export()
    nome = Nome(props.nome).export()
    extensao = props.extensao

    return Documento(DocumentoProps(id, nome, extensao))
