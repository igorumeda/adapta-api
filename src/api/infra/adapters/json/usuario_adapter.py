from src.shared.utils.json import ExtractJsonFrom

class UsuarioAdapter:
  def obter(self):
    return ExtractJsonFrom(__file__, "usuarios.json")