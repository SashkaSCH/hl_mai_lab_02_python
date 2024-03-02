import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"login": "test_user", "password": "test_password"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["login"] == "test_user"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["login"] == "test_user"
