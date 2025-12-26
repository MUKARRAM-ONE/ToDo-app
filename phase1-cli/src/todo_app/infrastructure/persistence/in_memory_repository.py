"""InMemoryTaskRepository - In-memory implementation of TaskRepository."""

from typing import Optional
from copy import deepcopy

from todo_app.application.interfaces.task_repository import TaskRepository
from todo_app.application.dto.task_filter import TaskFilter
from todo_app.application.exceptions import TaskNotFoundError
from todo_app.domain.entities.task import Task
from todo_app.domain.value_objects.task_id import TaskId


class InMemoryTaskRepository(TaskRepository):
    """In-memory implementation of TaskRepository.

    Stores tasks in a dictionary for fast O(1) access by ID.
    Suitable for Phase I requirements (no persistence needed).
    """

    def __init__(self) -> None:
        """Initialize empty repository."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, task: Task) -> Task:
        """Add a new task to the repository.

        Args:
            task: Task entity to add

        Returns:
            Task with assigned ID
        """
        # Assign new ID if needed
        task_copy = deepcopy(task)
        task_copy.id = TaskId(value=self._next_id)
        self._tasks[self._next_id] = task_copy
        self._next_id += 1
        return task_copy

    def get_by_id(self, task_id: TaskId) -> Optional[Task]:
        """Retrieve task by ID.

        Args:
            task_id: The task identifier

        Returns:
            Task entity if found, None otherwise
        """
        return self._tasks.get(task_id.value)

    def get_all(self, task_filter: Optional[TaskFilter] = None) -> list[Task]:
        """Retrieve all tasks, optionally filtered.

        Args:
            task_filter: Optional filter criteria

        Returns:
            List of Task entities matching filter
        """
        tasks = list(self._tasks.values())
        
        if task_filter and task_filter.status is not None:
            tasks = [t for t in tasks if task_filter.matches(t.status)]
        
        return tasks

    def update(self, task: Task) -> Task:
        """Update existing task.

        Args:
            task: Task entity with updated values

        Returns:
            Updated task entity

        Raises:
            TaskNotFoundError: If task ID doesn't exist
        """
        if task.id.value not in self._tasks:
            raise TaskNotFoundError(task.id.value)
        
        self._tasks[task.id.value] = task
        return task

    def delete(self, task_id: str) -> None:
        """Delete task by ID (accepts string).

        Args:
            task_id: The task identifier as string

        Raises:
            TaskNotFoundError: If task ID doesn't exist
        """
        try:
            int_id = int(task_id)
            if int_id not in self._tasks:
                raise TaskNotFoundError(int_id)
            
            del self._tasks[int_id]
        except ValueError:
            raise TaskNotFoundError(task_id)

    def count(self, task_filter: Optional[TaskFilter] = None) -> int:
        """Count tasks, optionally filtered.

        Args:
            task_filter: Optional filter criteria

        Returns:
            Number of matching tasks
        """
        return len(self.get_all(task_filter))

    def find_by_id(self, task_id: str) -> Optional[Task]:
        """Find task by string ID (convenience method).
        
        Args:
            task_id: Task ID as string
            
        Returns:
            Task entity if found, None otherwise
        """
        try:
            int_id = int(task_id)
            return self._tasks.get(int_id)
        except (ValueError, AttributeError):
            return None

    def find_all(self, task_filter: TaskFilter) -> list[Task]:
        """Find all tasks matching filter (convenience method).
        
        Args:
            task_filter: Filter criteria
            
        Returns:
            List of matching tasks
        """
        return self.get_all(task_filter)
