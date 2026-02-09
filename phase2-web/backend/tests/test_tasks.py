from fastapi.testclient import TestClient
from app.utils.auth import create_access_token

def test_create_task(client: TestClient):
    user_id = "test-user-1"
    token = create_access_token({"sub": user_id})
    headers = {"Authorization": f"Bearer {token}"}
    
    response = client.post(
        f"/api/tasks/{user_id}/tasks",
        json={"title": "Test Task", "description": "Test Desc"},
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["user_id"] == user_id

def test_get_tasks_isolation(client: TestClient):
    # Create task for user 1
    user1_id = "user-1"
    token1 = create_access_token({"sub": user1_id})
    client.post(
        f"/api/tasks/{user1_id}/tasks",
        json={"title": "User 1 Task"},
        headers={"Authorization": f"Bearer {token1}"}
    )
    
    # Attempt to access user 1 tasks with user 2 token
    user2_id = "user-2"
    token2 = create_access_token({"sub": user2_id})
    response = client.get(
        f"/api/tasks/{user1_id}/tasks",
        headers={"Authorization": f"Bearer {token2}"}
    )
    assert response.status_code == 403
    assert response.json()["detail"] == "Not authorized to access these tasks"
