
from fastapi import FastAPI

from app.routes import multiply
app = FastAPI()



@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a mi API de Usuarios, Gerardi Nimrod!"}


app.include_router(multiply.router)
