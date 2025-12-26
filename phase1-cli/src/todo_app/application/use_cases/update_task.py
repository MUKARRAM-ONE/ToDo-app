"""Update task use case."""

from typing import Optional
from todo_app.application.interfaces.task_repository import TaskRepository
from todo_app.application.dto.task_dto import TaskDTO
from todo_app.application.exceptions import TaskNotFoundError
from todo_app.domain.value_objects.task_title import TaskTitle
from todo_app.domain.value_objects.task_description import TaskDescription


class UpdateTaskUseCase:
    """Use case for updating task details."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize the use case.
        
        Args:
            repository: Task repository implementation
        """
        self._repository = repository

    def execute(
        self,
        task_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> TaskDTO:
        """Execute the update task use case.
        
        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)
            
        Returns:
            TaskDTO with updated information
            
        Raises:
            TaskNotFoundError: If task with given ID doesn't exist
            ValueError: If task_id is invalid or no updates provided
        """
        if not task_id or not task_id.strip():
            raise ValueError("Task ID cannot be empty")
        
        if title is None and description is None:
            raise ValueError("At least one field (title or description) must be provided")
        
        # Get the task
        task = self._repository.find_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task with ID '{task_id}' not found")
        
        # Update title if provided
        if title is not None:
            new_title = TaskTitle(value=title)
            task.update_title(new_title)
        
        # Update description if provided
        if description is not None:
            new_description = TaskDescription(value=description)
            task.update_description(new_description)
        
        # Update in repository
        updated_task = self._repository.update(task)
        
        # Return DTO
        return TaskDTO.from_entity(updated_task)
