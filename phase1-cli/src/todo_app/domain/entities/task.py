"""Task entity - Core domain entity representing a todo task."""

from datetime import datetime
from pydantic import BaseModel, Field

from todo_app.domain.value_objects.task_id import TaskId
from todo_app.domain.value_objects.task_title import TaskTitle
from todo_app.domain.value_objects.task_description import TaskDescription
from todo_app.domain.enums.task_status import TaskStatus


class Task(BaseModel):
    """Task entity representing a todo item.

    This is the aggregate root for the task domain.
    Contains business logic for task state management.
    """

    id: TaskId = Field(description="Unique task identifier")
    title: TaskTitle = Field(description="Task title (1-100 characters)")
    description: TaskDescription = Field(
        default_factory=lambda: TaskDescription(value=""),
        description="Optional task description (0-500 characters)"
    )
    status: TaskStatus = Field(default=TaskStatus.PENDING, description="Task completion status")
    created_at: datetime = Field(default_factory=datetime.now, description="Task creation timestamp")

    # Allow mutation for update operations
    model_config = {"frozen": False}

    def toggle_status(self) -> None:
        """Toggle task status between PENDING and COMPLETE."""
        if self.status == TaskStatus.PENDING:
            self.status = TaskStatus.COMPLETE
        else:
            self.status = TaskStatus.PENDING

    def update_title(self, new_title: TaskTitle) -> None:
        """Update task title.

        Args:
            new_title: The new title value object
        """
        self.title = new_title

    def update_description(self, new_description: TaskDescription) -> None:
        """Update task description.

        Args:
            new_description: The new description value object
        """
        self.description = new_description

    def is_complete(self) -> bool:
        """Check if task is marked as complete.

        Returns:
            True if task status is COMPLETE, False otherwise
        """
        return self.status == TaskStatus.COMPLETE

    def is_pending(self) -> bool:
        """Check if task is pending completion.

        Returns:
            True if task status is PENDING, False otherwise
        """
        return self.status == TaskStatus.PENDING
