from fastapi import FastAPI

from app.routes import multiply
from app.services.usuario_service import UsuarioService

app = FastAPI()
service = UsuarioService()


@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a mi API de Usuarios, Anthony!"}


app.include_router(multiply.router)
