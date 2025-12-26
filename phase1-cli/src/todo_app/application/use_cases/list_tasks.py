"""List tasks use case."""

from typing import List
from todo_app.application.interfaces.task_repository import TaskRepository
from todo_app.application.dto.task_dto import TaskDTO
from todo_app.application.dto.task_filter import TaskFilter


class ListTasksUseCase:
    """Use case for listing tasks with optional filtering."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize the use case.
        
        Args:
            repository: Task repository implementation
        """
        self._repository = repository

    def execute(self, filter_status: str = "all") -> List[TaskDTO]:
        """Execute the list tasks use case.
        
        Args:
            filter_status: Filter by status ("all", "pending", "complete")
            
        Returns:
            List of TaskDTO objects matching the filter
            
        Raises:
            ValueError: If filter_status is invalid
        """
        # Validate filter
        valid_filters = ["all", "pending", "complete"]
        if filter_status not in valid_filters:
            raise ValueError(
                f"Invalid filter status: {filter_status}. "
                f"Must be one of: {', '.join(valid_filters)}"
            )
        
        # Create filter object
        task_filter = TaskFilter(status=filter_status)
        
        # Get filtered tasks
        tasks = self._repository.find_all(task_filter)
        
        # Convert to DTOs
        return [TaskDTO.from_entity(task) for task in tasks]
