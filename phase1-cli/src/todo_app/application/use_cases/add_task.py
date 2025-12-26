"""AddTaskUseCase - Create new tasks."""

from datetime import datetime

from todo_app.application.interfaces.task_repository import TaskRepository
from todo_app.application.dto.task_dto import TaskDTO
from todo_app.domain.entities.task import Task
from todo_app.domain.value_objects.task_id import TaskId
from todo_app.domain.value_objects.task_title import TaskTitle
from todo_app.domain.value_objects.task_description import TaskDescription
from todo_app.domain.enums.task_status import TaskStatus


class AddTaskUseCase:
    """Use case for adding a new task."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize use case with repository.

        Args:
            repository: Task repository implementation
        """
        self._repository = repository

    def execute(self, title: str, description: str = "") -> TaskDTO:
        """Execute the add task use case.

        Args:
            title: Task title (1-100 characters)
            description: Optional task description (0-500 characters)

        Returns:
            TaskDTO representing the created task

        Raises:
            ValidationError: If title or description validation fails
        """
        # Create domain entities with validation
        task_title = TaskTitle(value=title)
        task_desc = TaskDescription(value=description)
        
        # Create task entity (ID will be assigned by repository)
        task = Task(
            id=TaskId(value=1),  # Placeholder, will be reassigned
            title=task_title,
            description=task_desc,
            status=TaskStatus.PENDING,
            created_at=datetime.now()
        )
        
        # Persist through repository
        saved_task = self._repository.add(task)
        
        # Return DTO
        return TaskDTO.from_entity(saved_task)
