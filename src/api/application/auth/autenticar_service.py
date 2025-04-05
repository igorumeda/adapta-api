from src.api.core.application_service import ApplicationService

class AutenticarService(ApplicationService):
    def __init__(self):
        self.user_repository = user_repository
        self.token_provider = token_provider

    def handle(self, cpf: str, senha: str) -> object:
        usuario = self.user_repository.buscar_por_cpf(cpf)
        if not usuario or not usuario.validar_senha(senha):
            raise Unauthorized("Credenciais inválidas")

        access_token = self.token_provider.gerar_access_token(cpf)
        refresh_token = self.token_provider.gerar_refresh_token(cpf)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
