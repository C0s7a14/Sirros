from fastapi.testclient import TestClient

import pytest

from app.main import app as fastapi_app

client = TestClient(fastapi_app)


def test_list_quizzes_empty(setup_db):
    response = client.get("/quizzes")
    assert response.status_code == 200
    assert response.json() == []


def test_create_quiz(setup_db):
    training = client.post("/trainings", json={"title": "T", "description": ""}).json()
    response = client.post("/quizzes", json={"training_id": training["id"], "title": "Quiz 1"})
    assert response.status_code == 201
    assert response.json()["title"] == "Quiz 1"


def test_get_quiz_not_found(setup_db):
    response = client.get("/quizzes/id-inexistente")
    assert response.status_code == 404
