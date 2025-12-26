"""TaskStatus enumeration - Task completion states."""

from enum import Enum


class TaskStatus(str, Enum):
    """Task status enumeration.

    Represents the completion state of a task.
    """

    PENDING = "pending"
    COMPLETE = "complete"

    def symbol(self) -> str:
        """Get display symbol for status.

        Returns:
            Unicode symbol representing status
        """
        return "✓" if self == TaskStatus.COMPLETE else "○"

    def color(self) -> str:
        """Get Rich color code for status.

        Returns:
            Color name for Rich formatting
        """
        return "green" if self == TaskStatus.COMPLETE else "yellow"
