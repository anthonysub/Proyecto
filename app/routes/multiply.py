from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/multiply")
def multiply(
    num1: float = Query(..., description="Primer número"),
    num2: float = Query(..., description="Segundo número"),
):
    return {"operation": "multiply", "num1": num1, "num2": num2, "result": num1 * num2}
