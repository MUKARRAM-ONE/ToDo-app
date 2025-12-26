"""TaskFilter - Filtering criteria for task queries."""

from typing import Optional
from pydantic import BaseModel, field_validator

from todo_app.domain.enums.task_status import TaskStatus


class TaskFilter(BaseModel):
    """Filter criteria for querying tasks.

    Attributes:
        status: Optional status filter ("all", "pending", "complete")
    """

    status: Optional[str] = None

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: Optional[str]) -> Optional[str]:
        """Validate status value.
        
        Args:
            v: Status value to validate
            
        Returns:
            Validated status value
            
        Raises:
            ValueError: If status is invalid
        """
        if v is None:
            return None
        
        valid = ["all", "pending", "complete"]
        if v.lower() not in valid:
            raise ValueError(f"Status must be one of: {', '.join(valid)}")
        
        return v.lower()

    def matches(self, task_status: TaskStatus) -> bool:
        """Check if a task status matches this filter.

        Args:
            task_status: The task status to check

        Returns:
            True if the status matches the filter, False otherwise
        """
        if self.status is None or self.status == "all":
            return True
        return task_status.value == self.status
