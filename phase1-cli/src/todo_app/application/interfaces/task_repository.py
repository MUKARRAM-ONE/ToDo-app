"""TaskRepository interface - Abstract repository contract."""

from abc import ABC, abstractmethod
from typing import Optional

from todo_app.domain.entities.task import Task
from todo_app.domain.value_objects.task_id import TaskId
from todo_app.application.dto.task_filter import TaskFilter


class TaskRepository(ABC):
    """Abstract repository interface for Task entities.

    Defines the contract for task persistence operations.
    """

    @abstractmethod
    def add(self, task: Task) -> Task:
        """Add a new task to the repository.

        Args:
            task: Task entity to add (ID may be reassigned)

        Returns:
            Task with assigned ID

        Raises:
            RepositoryError: If add operation fails
        """
        pass

    @abstractmethod
    def get_by_id(self, task_id: TaskId) -> Optional[Task]:
        """Retrieve task by ID.

        Args:
            task_id: The task identifier

        Returns:
            Task entity if found, None otherwise
        """
        pass

    @abstractmethod
    def get_all(self, task_filter: Optional[TaskFilter] = None) -> list[Task]:
        """Retrieve all tasks, optionally filtered.

        Args:
            task_filter: Optional filter criteria

        Returns:
            List of Task entities matching filter
        """
        pass

    @abstractmethod
    def update(self, task: Task) -> None:
        """Update existing task.

        Args:
            task: Task entity with updated values

        Raises:
            TaskNotFoundError: If task ID doesn't exist
            RepositoryError: If update operation fails
        """
        pass

    @abstractmethod
    def delete(self, task_id: TaskId) -> None:
        """Delete task by ID.

        Args:
            task_id: The task identifier

        Raises:
            TaskNotFoundError: If task ID doesn't exist
            RepositoryError: If delete operation fails
        """
        pass

    @abstractmethod
    def count(self, task_filter: Optional[TaskFilter] = None) -> int:
        """Count tasks, optionally filtered.

        Args:
            task_filter: Optional filter criteria

        Returns:
            Number of matching tasks
        """
        pass
