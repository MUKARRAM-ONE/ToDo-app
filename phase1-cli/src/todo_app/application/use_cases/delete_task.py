"""Delete task use case."""

from todo_app.application.interfaces.task_repository import TaskRepository
from todo_app.application.exceptions import TaskNotFoundError


class DeleteTaskUseCase:
    """Use case for deleting a task."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize the use case.
        
        Args:
            repository: Task repository implementation
        """
        self._repository = repository

    def execute(self, task_id: str) -> None:
        """Execute the delete task use case.
        
        Args:
            task_id: ID of the task to delete
            
        Raises:
            TaskNotFoundError: If task with given ID doesn't exist
            ValueError: If task_id is invalid
        """
        if not task_id or not task_id.strip():
            raise ValueError("Task ID cannot be empty")
        
        # Check if task exists
        task = self._repository.find_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task with ID '{task_id}' not found")
        
        # Delete the task
        self._repository.delete(task_id)
