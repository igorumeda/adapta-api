from api.infra.adapters.json.usuario_adapter import UsuarioAdapter
from src.api.core.application_service import ApplicationService

class ObterUsuariosService(ApplicationService):
  def __init__(self) -> None:
    self.adapter = UsuarioAdapter()
    
  def handle(self):
    return self.adapter.obter()