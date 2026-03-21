# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_multiply():
    response = client.get("/multiplicacion?num1=10&num2=5")
    assert response.status_code == 200
    print(f"\nRespuesta de la API: {response.json()}")
    assert response.json()["resultado"] == 50.0


def test_suma():
    response = client.get("/suma?num1=10&num2=5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 15.0
    print(f"\nRespuesta de la API: {response.json()}")


def test_division():
    response = client.get("/division?num1=10&num2=5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 2.0
    print(f"\nRespuesta de la API: {response.json()}")

def test_resta():
    response = client.get("/resta?num1=10&num2=5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5.0
    print(f"\nRespuesta de la API: {response.json()}")