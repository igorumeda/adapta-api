from src.api.infra.adapters.json.usuario_adapter import UsuarioAdapter
from src.api.core.application_service import ApplicationService

class ObterUsuariosService(ApplicationService):
  def __init__(self) -> None:
    self.adapter = UsuarioAdapter()
    
  def handle(self, cpf: str):
    return self.adapter.obterPor(cpf)