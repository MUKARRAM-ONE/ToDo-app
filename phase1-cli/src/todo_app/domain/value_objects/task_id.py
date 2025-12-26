"""TaskId value object - Type-safe task identifier."""

from pydantic import BaseModel, Field, field_validator


class TaskId(BaseModel, frozen=True):
    """Task identifier value object.

    Ensures task IDs are always positive integers.
    Immutable once created.
    """

    value: int = Field(gt=0, description="Positive integer task identifier")

    @field_validator("value")
    @classmethod
    def validate_positive(cls, v: int) -> int:
        """Validate that value is greater than 0.

        Args:
            v: The value to validate

        Returns:
            The validated value

        Raises:
            ValueError: If value is not greater than 0
        """
        if v <= 0:
            raise ValueError("Task ID must be greater than 0")
        return v
