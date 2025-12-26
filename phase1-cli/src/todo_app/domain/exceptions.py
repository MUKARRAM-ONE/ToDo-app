"""Domain layer exceptions."""

class TodoAppError(Exception):
    """Base exception for all application errors."""

    pass


class DomainError(TodoAppError):
    """Base exception for domain layer errors."""

    pass


class ValidationError(DomainError):
    """Exception raised when domain validation fails."""

    def __init__(self, field: str, message: str) -> None:
        """Initialize validation error.

        Args:
            field: The field that failed validation
            message: The validation error message
        """
        self.field = field
        self.message = message
        super().__init__(f"Validation error for '{field}': {message}")
