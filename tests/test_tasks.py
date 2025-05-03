import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.models.task import Task
from app.models.user import User
from app.core.security import get_password_hash

client = TestClient(app)

@pytest.fixture
def test_user(db: Session):
    user = User(
        email="test@example.com",
        hashed_password=get_password_hash("testpassword"),
        full_name="Test User"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@pytest.fixture
def test_task(db: Session, test_user: User):
    task = Task(
        title="Test Task",
        description="Test Description",
        user_id=test_user.id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def test_create_task(db: Session, test_user: User):
    response = client.post(
        "/api/v1/tasks/",
        json={
            "title": "New Task",
            "description": "New Description",
            "status": "pending",
            "priority": "medium"
        },
        headers={"Authorization": f"Bearer {get_access_token(test_user)}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Task"
    assert data["description"] == "New Description"

def test_read_tasks(db: Session, test_user: User, test_task: Task):
    response = client.get(
        "/api/v1/tasks/",
        headers={"Authorization": f"Bearer {get_access_token(test_user)}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["title"] == test_task.title

def test_update_task(db: Session, test_user: User, test_task: Task):
    response = client.put(
        f"/api/v1/tasks/{test_task.id}",
        json={
            "title": "Updated Task",
            "status": "completed"
        },
        headers={"Authorization": f"Bearer {get_access_token(test_user)}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["status"] == "completed"

def test_delete_task(db: Session, test_user: User, test_task: Task):
    response = client.delete(
        f"/api/v1/tasks/{test_task.id}",
        headers={"Authorization": f"Bearer {get_access_token(test_user)}"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"

def get_access_token(user: User) -> str:
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": user.email,
            "password": "testpassword"
        }
    )
    return response.json()["access_token"] 