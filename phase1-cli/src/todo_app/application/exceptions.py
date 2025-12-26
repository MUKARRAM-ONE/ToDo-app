"""Application layer exceptions."""

from todo_app.domain.exceptions import TodoAppError


class ApplicationError(TodoAppError):
    """Base exception for application layer errors."""

    pass


class TaskNotFoundError(ApplicationError):
    """Exception raised when a task cannot be found."""

    def __init__(self, task_id: int) -> None:
        """Initialize task not found error.

        Args:
            task_id: The ID of the task that was not found
        """
        self.task_id = task_id
        super().__init__(f"Task ID {task_id} not found")


class InvalidOperationError(ApplicationError):
    """Exception raised when an invalid operation is attempted."""

    pass
