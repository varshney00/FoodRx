from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_get_all_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert "recipes" in response.json()

def test_get_recipes_by_diet():
    response = client.get("/recipes/?diet=vegan")
    assert response.status_code == 200
    assert isinstance(response.json()["recipes"], list)
