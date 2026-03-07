from fastapi import FastAPI
from app.services.usuario_service import UsuarioService

app = FastAPI()
service = UsuarioService()

@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a mi API de Usuarios, Anthony!"}

@app.get("/usuarios")
def listar_usuarios():
    # Esto devolverá la lista de usuarios que creamos en tu lógica
    return service.obtener_usuarios()

@app.post("/usuarios")
def crear_usuario(usuario: UsuarioCreate):
    service.crear_usuario(usuario.nombre)
    return {"status": "Usuario creado"}

@app.get("/usuarios/{nombre}")
def test(nombre: str):
    return {"nombre": nombre}
    xd