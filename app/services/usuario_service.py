from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository
 
 
class UsuarioService:
    def __init__(self, repo=None):
        self.repo = repo if repo else UsuarioRepository()
 
    def crear_usuario(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
 
        usuario = Usuario(nombre)
        self.repo.guardar(usuario)
 
    def obtener_usuarios(self):
        return self.repo.listar()