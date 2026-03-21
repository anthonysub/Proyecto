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


@router.get("/division")
def division(
    num1: float = Query(..., description="Primer número"),
    num2: float = Query(..., description="Segundo número"),
    
):
    if num2 == 0 or num1 == 0:
        return {"error": "No se puede dividir por cero"}
    return {"operacion": "division", "num1": num1, "num2": num2, "resultado": num1 / num2}

@router.get("/resta")
def resta(
    num1: float = Query(..., description="Primer número"),
    num2: float = Query(..., description="Segundo número"),
    
):
    """
    Realiza la resta de dos números.
    
    Parámetros:
    - num1: Minuendo (primer número)
    - num2: Sustraendo (segundo número)
    
    Retorna el resultado de num1 - num2
    """
    return {"operacion": "resta", "num1": num1, "num2": num2, "resultado": num1 - num2}
