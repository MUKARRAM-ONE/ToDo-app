"""Toggle task status use case."""

from todo_app.application.interfaces.task_repository import TaskRepository
from todo_app.application.dto.task_dto import TaskDTO
from todo_app.application.exceptions import TaskNotFoundError


class ToggleTaskUseCase:
    """Use case for toggling task completion status."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize the use case.
        
        Args:
            repository: Task repository implementation
        """
        self._repository = repository

    def execute(self, task_id: str) -> TaskDTO:
        """Execute the toggle task use case.
        
        Args:
            task_id: ID of the task to toggle
            
        Returns:
            TaskDTO with updated status
            
        Raises:
            TaskNotFoundError: If task with given ID doesn't exist
            ValueError: If task_id is invalid
        """
        if not task_id or not task_id.strip():
            raise ValueError("Task ID cannot be empty")
        
        # Get the task
        task = self._repository.find_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task with ID '{task_id}' not found")
        
        # Toggle status
        task.toggle_status()
        
        # Update in repository
        updated_task = self._repository.update(task)
        
        # Return DTO
        return TaskDTO.from_entity(updated_task)
