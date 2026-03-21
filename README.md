# Proyecto

## Descripción
API REST con operaciones matemáticas básicas construida con FastAPI.

## Funciones - multiply.py

### 1. `multiply(num1, num2)`
Realiza la multiplicación de dos números.

**Parámetros:**
- `num1` (float): Primer número
- `num2` (float): Segundo número

**Retorna:**
```json
{
  "operacion": "multiplicacion",
  "num1": 5.0,
  "num2": 3.0,
  "resultado": 15.0
}
```

**Endpoint:** `GET /multiplicacion?num1=5&num2=3`

---

### 2. `suma(num1, num2)`
Realiza la suma de dos números.

**Parámetros:**
- `num1` (float): Primer número
- `num2` (float): Segundo número

**Retorna:**
```json
{
  "operacion": "la suma es",
  "num1": 5.0,
  "num2": 3.0,
  "resultado": 8.0
}
```

**Endpoint:** `GET /suma?num1=5&num2=3`

---

### 3. `division(num1, num2)`
Realiza la división de dos números con validación para evitar división por cero.

**Parámetros:**
- `num1` (float): Primer número (dividendo)
- `num2` (float): Segundo número (divisor)

**Retorna:**
```json
{
  "operacion": "division",
  "num1": 10.0,
  "num2": 2.0,
  "resultado": 5.0
}
```

**Error:**
```json
{
  "error": "No se puede dividir por cero"
}
```

**Endpoint:** `GET /division?num1=10&num2=2`


### 4. `resta(num1, num2)`
Realiza la multiplicación de dos números.

**Parámetros:**
- `num1` (float): Primer número
- `num2` (float): Segundo número

**Retorna:**
```json
{
  "operacion": "resta",
  "num1": 5.0,
  "num2": 3.0,
  "resultado": 2.0
}
```

**Endpoint:** `GET /resta?num1=5&num2=3`
