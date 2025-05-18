import pytest
from rest_framework.test import APIClient
from tasks.models import Task

pytestmark = pytest.mark.django_db

def test_create_task():
    client = APIClient()
    response = client.post("/api/tasks/", {"title": "Aprender Pytest", "completed": False})
    assert response.status_code == 201
    assert Task.objects.first().title == "Aprender Pytest"