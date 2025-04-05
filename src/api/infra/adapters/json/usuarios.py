from src.shared.utils.json import ExtractJsonFrom

class UsuariosAdapter:
  def obter(self):
    return ExtractJsonFrom(__file__, "usuarios.json")