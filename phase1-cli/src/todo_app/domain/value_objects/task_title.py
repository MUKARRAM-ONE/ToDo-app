"""TaskTitle value object - Validated task title."""

from pydantic import BaseModel, Field, field_validator


class TaskTitle(BaseModel, frozen=True):
    """Task title value object.

    Ensures titles are 1-100 characters, non-empty, with whitespace stripped.
    Immutable once created.
    """

    value: str = Field(min_length=1, max_length=100, description="Task title (1-100 characters)")

    @field_validator("value")
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        """Validate that title is not empty or whitespace-only.

        Args:
            v: The value to validate

        Returns:
            The stripped and validated value

        Raises:
            ValueError: If value is empty or only whitespace
        """
        stripped = v.strip()
        if not stripped:
            raise ValueError("Title cannot be empty or only whitespace")
        return stripped

    @field_validator("value")
    @classmethod
    def validate_length(cls, v: str) -> str:
        """Validate that title length is within bounds.

        Args:
            v: The value to validate

        Returns:
            The validated value

        Raises:
            ValueError: If value exceeds 100 characters
        """
        if len(v) > 100:
            raise ValueError(f"Title cannot exceed 100 characters (got {len(v)})")
        return v
