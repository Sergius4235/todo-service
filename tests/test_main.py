from fastapi.testclient import TestClient
from app.main import app

test_client = TestClient(app)

def test_get_tasks():
    response = test_client.get("/tasks")
    assert response.status_code == 200
