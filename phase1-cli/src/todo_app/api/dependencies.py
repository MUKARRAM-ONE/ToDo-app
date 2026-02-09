"""FastAPI dependencies for dependency injection."""

from fastapi import Request
from todo_app.application.interfaces.task_repository import TaskRepository

def get_repository(request: Request) -> TaskRepository:
    """Get repository instance from application state."""
    return request.app.state.repository
