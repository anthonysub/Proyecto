class UsuarioRepository:
    def __init__(self):
        self.usuarios = []
 
    def guardar(self, usuario):
        self.usuarios.append(usuario)
 
    def listar(self):
        return self.usuarios