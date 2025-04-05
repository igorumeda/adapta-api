from src.api.infra.adapters.json.usuarios import UsuariosAdapter
from src.api.core.application_service import ApplicationService

class ObterUsuariosService(ApplicationService):
  def __init__(self) -> None:
    self.adapter = UsuariosAdapter()
    
  def handle(self):
    return self.adapter.obter()