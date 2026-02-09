"""Pydantic schemas for Task API."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from todo_app.application.dto.task_dto import TaskDTO

class TaskCreateRequest(BaseModel):
    """Request schema for creating a task."""
    
    title: str = Field(..., min_length=1, max_length=100, description="Task title")
    description: str = Field(default="", max_length=500, description="Task description")

class TaskUpdateRequest(BaseModel):
    """Request schema for updating a task."""
    
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class TaskResponse(BaseModel):
    """Response schema for a task."""
    
    id: int
    title: str
    description: str
    status: str
    created_at: datetime
    
    @classmethod
    def from_dto(cls, dto: TaskDTO) -> "TaskResponse":
        """Create response from DTO."""
        return cls(
            id=dto.id,
            title=dto.title,
            description=dto.description,
            status=dto.status,
            created_at=dto.created_at
        )

class TaskListResponse(BaseModel):
    """Response schema for task list."""
    
    tasks: list[TaskResponse] = Field(default_factory=list)
    total: int
