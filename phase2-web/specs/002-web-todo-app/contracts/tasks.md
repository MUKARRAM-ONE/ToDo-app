# API Contract: Tasks

## GET /api/{user_id}/tasks
- **Description**: List all tasks for a specific user.
- **Headers**: `Authorization: Bearer <token>`
- **Query Params**: `status` (optional: all|pending|completed)
- **Success Response (200)**:
  ```json
  [
    {
      "id": 1,
      "title": "Task 1",
      "description": "Details",
      "completed": false,
      "created_at": "timestamp",
      "updated_at": "timestamp"
    }
  ]
  ```

## POST /api/{user_id}/tasks
- **Description**: Create a new task.
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "title": "New Task",
    "description": "Optional details"
  }
  ```
- **Success Response (201)**:
  ```json
  {
    "id": 2,
    "title": "New Task",
    "description": "Optional details",
    "completed": false,
    "created_at": "timestamp"
  }
  ```

## PUT /api/{user_id}/tasks/{id}
- **Description**: Update an existing task.
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "title": "Updated Title",
    "description": "Updated details"
  }
  ```
- **Success Response (200)**:
  ```json
  {
    "id": 1,
    "title": "Updated Title",
    "description": "Updated details",
    "completed": false,
    "updated_at": "timestamp"
  }
  ```

## DELETE /api/{user_id}/tasks/{id}
- **Description**: Delete a task.
- **Headers**: `Authorization: Bearer <token>`
- **Success Response (200)**:
  ```json
  { "success": true }
  ```

## PATCH /api/{user_id}/tasks/{id}/complete
- **Description**: Toggle task completion status.
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  { "completed": true }
  ```
- **Success Response (200)**:
  ```json
  { "id": 1, "completed": true }
  ```
