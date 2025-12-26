"""Tests for TaskId value object."""

import pytest
from pydantic import ValidationError


def test_task_id_valid_positive_integer() -> None:
    """Test TaskId accepts positive integers."""
    from todo_app.domain.value_objects.task_id import TaskId
    
    task_id = TaskId(value=1)
    assert task_id.value == 1


def test_task_id_zero_invalid() -> None:
    """Test TaskId rejects zero."""
    from todo_app.domain.value_objects.task_id import TaskId
    
    with pytest.raises(ValidationError) as exc_info:
        TaskId(value=0)
    
    assert "greater than 0" in str(exc_info.value).lower()


def test_task_id_negative_invalid() -> None:
    """Test TaskId rejects negative numbers."""
    from todo_app.domain.value_objects.task_id import TaskId
    
    with pytest.raises(ValidationError) as exc_info:
        TaskId(value=-1)
    
    assert "greater than 0" in str(exc_info.value).lower()


def test_task_id_immutable() -> None:
    """Test TaskId is immutable (frozen)."""
    from todo_app.domain.value_objects.task_id import TaskId
    
    task_id = TaskId(value=1)
    
    with pytest.raises((ValidationError, AttributeError)):
        task_id.value = 2  # type: ignore


def test_task_id_equality() -> None:
    """Test TaskId equality by value."""
    from todo_app.domain.value_objects.task_id import TaskId
    
    task_id_1 = TaskId(value=1)
    task_id_2 = TaskId(value=1)
    task_id_3 = TaskId(value=2)
    
    assert task_id_1 == task_id_2
    assert task_id_1 != task_id_3
