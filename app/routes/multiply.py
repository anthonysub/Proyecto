from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/multiplicacion")
def multiply(
    num1: float = Query(..., description="Primer número"),
    num2: float = Query(..., description="Segundo número"),
):
    return {"operacion": "multiplicacion", "num1": num1, "num2": num2, "resultado": num1 * num2}
@router.get("/suma")
def suma(
    num1: float = Query(..., description="Primer número"),
    num2: float = Query(..., description="Segundo número"),
):
    return {"operacion": "la suma es", "num1": num1, "num2": num2, "resultado": num1 + num2}