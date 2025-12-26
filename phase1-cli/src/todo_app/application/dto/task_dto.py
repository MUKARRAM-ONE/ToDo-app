"""TaskDTO - Data Transfer Object for Task entity."""

from datetime import datetime
from pydantic import BaseModel, Field

from todo_app.domain.entities.task import Task
from todo_app.domain.value_objects.task_id import TaskId
from todo_app.domain.value_objects.task_title import TaskTitle
from todo_app.domain.value_objects.task_description import TaskDescription
from todo_app.domain.enums.task_status import TaskStatus


class TaskDTO(BaseModel):
    """Data Transfer Object for Task entity.

    Used for transporting task data across layer boundaries.
    """

    id: str = Field(description="Task identifier")
    title: str = Field(description="Task title")
    description: str = Field(description="Task description")
    status: str = Field(description="Task status (pending/complete)")
    created_at: str = Field(description="Creation timestamp (ISO 8601)")

    @classmethod
    def from_entity(cls, task: Task) -> "TaskDTO":
        """Convert Task entity to DTO.

        Args:
            task: The Task entity to convert

        Returns:
            TaskDTO representation of the entity
        """
        return cls(
            id=str(task.id.value),
            title=task.title.value,
            description=task.description.value,
            status=task.status.value,
            created_at=task.created_at.isoformat()
        )

    def to_entity(self) -> Task:
        """Convert DTO to Task entity.

        Returns:
            Task entity from this DTO
        """
        return Task(
            id=TaskId(value=int(self.id)),
            title=TaskTitle(value=self.title),
            description=TaskDescription(value=self.description),
            status=TaskStatus(self.status),
            created_at=datetime.fromisoformat(self.created_at)
        )
