"""TaskDescription value object - Validated task description."""

from pydantic import BaseModel, Field, field_validator


class TaskDescription(BaseModel, frozen=True):
    """Task description value object.

    Ensures descriptions are 0-500 characters, with whitespace stripped.
    Empty string is allowed.
    Immutable once created.
    """

    value: str = Field(default="", max_length=500, description="Task description (0-500 characters)")

    @field_validator("value")
    @classmethod
    def strip_whitespace(cls, v: str) -> str:
        """Strip leading and trailing whitespace.

        Args:
            v: The value to validate

        Returns:
            The stripped value
        """
        return v.strip()

    @field_validator("value")
    @classmethod
    def validate_length(cls, v: str) -> str:
        """Validate that description length is within bounds.

        Args:
            v: The value to validate

        Returns:
            The validated value

        Raises:
            ValueError: If value exceeds 500 characters
        """
        if len(v) > 500:
            raise ValueError(f"Description cannot exceed 500 characters (got {len(v)})")
        return v
