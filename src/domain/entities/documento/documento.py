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
      super().state.id.export(), 
      super().state.nome.export(),
      super().state.extensao
    )
  
  def _parse(self, props):
    id = Id(props.id)
    nome = Nome(props.nome)
    extensao = props.extensao

    return Documento({id, nome, extensao})
