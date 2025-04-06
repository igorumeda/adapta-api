import json
from typing import List
from src.domain.entities.usuario.usuario import Usuario, UsuarioProps
from src.shared.utils.json import ExtractJsonFrom

class UsuarioAdapter:
  def obterPor(self, cpf: str) -> Usuario | None:
    usuarioData = ExtractJsonFrom(__file__, "usuarios.json")
    usuarioProps: List[UsuarioProps] = json.loads(usuarioData)
    
    for usuario in usuarioProps:
      if usuario.cpf == cpf:
        return Usuario(UsuarioProps(
          usuario.id,
          usuario.nome,
          usuario.cpf,
          usuario.email,
          usuario.senha
        ))
    