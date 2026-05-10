import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.modules.trainings.models import Training

client = TestClient(app)


def test_list_trainings_empty(setup_db):
    response = client.get("/trainings")
    assert response.status_code == 200
    assert response.json() == []


def test_create_training(setup_db):
    response = client.post("/trainings", json={"title": "Treinamento A", "description": "Desc"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Treinamento A"
    assert "id" in data


def test_get_training_not_found(setup_db):
    response = client.get("/trainings/id-inexistente")
    assert response.status_code == 404


def test_update_training(setup_db):
    created = client.post("/trainings", json={"title": "Original", "description": ""}).json()
    response = client.put(f"/trainings/{created['id']}", json={"title": "Atualizado"})
    assert response.status_code == 200
    assert response.json()["title"] == "Atualizado"


def test_delete_training(setup_db):
    created = client.post("/trainings", json={"title": "Para deletar", "description": ""}).json()
    response = client.delete(f"/trainings/{created['id']}")
    assert response.status_code == 204
    assert client.get(f"/trainings/{created['id']}").status_code == 404
