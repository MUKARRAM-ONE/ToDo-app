"""
# Todo Application - FastAPI Integration

This application demonstrates an object-oriented approach with FastAPI integration.

## Architecture

The application follows Clean Architecture principles:

### Domain Layer
- **Entities**: `Task` - Core business entity
- **Value Objects**: `TaskId`, `TaskTitle`, `TaskDescription`
- **Enums**: `TaskStatus` (PENDING, COMPLETE)

### Application Layer
- **Use Cases**: Business logic operations
  - `AddTaskUseCase` - Create tasks
  - `ListTasksUseCase` - Retrieve tasks
  - `UpdateTaskUseCase` - Modify tasks
  - `ToggleTaskUseCase` - Change task status
  - `DeleteTaskUseCase` - Remove tasks
- **DTOs**: Data Transfer Objects
- **Interfaces**: Repository abstractions

### Infrastructure Layer
- **Persistence**: `InMemoryTaskRepository` - In-memory storage
- **CLI**: Click-based console interface
- **API**: FastAPI REST interface

## Running the Applications

### 1. CLI Mode (Console)
```bash
# Interactive mode
python -m todo_app.interactive

# Command-line mode
todo list
todo add "Buy groceries"
todo toggle 1
```

### 2. FastAPI Server
```bash
# Using the command
todo-api

# Or directly
python -m todo_app.api.server

# Or with uvicorn
uvicorn todo_app.api.main:app --reload
```

### 3. API Documentation
Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Tasks
- `POST /api/tasks` - Create a new task
- `GET /api/tasks` - List all tasks (optional status filter)
- `GET /api/tasks/{id}` - Get a specific task
- `PUT /api/tasks/{id}` - Update a task
- `PATCH /api/tasks/{id}/toggle` - Toggle task completion
- `DELETE /api/tasks/{id}` - Delete a task

### Example Usage

#### Create Task
```bash
curl -X POST "http://localhost:8000/api/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

#### List Tasks
```bash
# All tasks
curl "http://localhost:8000/api/tasks"

# Only pending tasks
curl "http://localhost:8000/api/tasks?status_filter=pending"

# Only completed tasks
curl "http://localhost:8000/api/tasks?status_filter=complete"
```

#### Toggle Task
```bash
curl -X PATCH "http://localhost:8000/api/tasks/1/toggle"
```

#### Update Task
```bash
curl -X PUT "http://localhost:8000/api/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries and supplies", "description": "Milk, eggs, bread, soap"}'
```

#### Delete Task
```bash
curl -X DELETE "http://localhost:8000/api/tasks/1"
```

## Object-Oriented Design Patterns

### 1. Repository Pattern
Abstracts data access through `TaskRepository` interface with in-memory implementation.

### 2. Use Case Pattern
Each business operation is encapsulated in its own use case class.

### 3. Dependency Injection
FastAPI's dependency injection system provides repository instances to routes.

### 4. DTO Pattern
Data Transfer Objects separate API models from domain entities.

### 5. Value Objects
Enforces validation and domain rules at the type level.

## Installation

```bash
cd phase1-cli
pip install -e .
```

For development:
```bash
pip install -e ".[dev]"
```

## Benefits of This Architecture

1. **Separation of Concerns**: Each layer has clear responsibilities
2. **Testability**: Business logic is independent of frameworks
3. **Flexibility**: Easy to swap implementations (e.g., database instead of in-memory)
4. **Type Safety**: Pydantic models with validation
5. **Multiple Interfaces**: Same business logic for CLI and API

## Next Steps

This architecture is ready for:
- Database integration (PostgreSQL with SQLAlchemy)
- Authentication and authorization
- Next.js frontend integration
- Docker containerization
- Kubernetes deployment
