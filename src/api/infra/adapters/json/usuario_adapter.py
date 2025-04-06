from typing import List
from pydantic import parse_obj_as
from src.domain.entities.usuario.usuario import Usuario, UsuarioProps
from src.shared.utils.json import ExtractJsonFrom

class UsuarioAdapter:
  def obterPor(self, cpf: str) -> Usuario | None:
    usuarioData = ExtractJsonFrom(__file__, "usuarios.json")
    usuarioProps: List[UsuarioProps] = parse_obj_as(List[UsuarioProps], usuarioData)
    
    for usuario in usuarioProps:
      if usuario.cpf == cpf:
        return Usuario(UsuarioProps(
          usuario.id,
          usuario.nome,
          usuario.cpf,
          usuario.email,
          usuario.senha
        ))
    