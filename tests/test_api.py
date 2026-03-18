def test_multiply():
    from fastapi.testclient import TestClient

    from app.main import app

    client = TestClient(app)

    response = client.get("/multiply?num1=10&num2=5")
    assert response.status_code == 200
    assert response.json() == {
        "operation": "multiply",
        "num1": 10,
        "num2": 5,
        "result": 50,
    }
