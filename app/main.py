
from fastapi import FastAPI

from app.routes import multiply
app = FastAPI()



@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a mi API de Usuarios, Anthony!"}


app.include_router(multiply.router)
