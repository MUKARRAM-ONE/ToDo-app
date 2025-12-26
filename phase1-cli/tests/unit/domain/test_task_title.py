"""Tests for TaskTitle value object."""

import pytest
from pydantic import ValidationError


def test_task_title_valid() -> None:
    """Test TaskTitle accepts valid strings."""
    from todo_app.domain.value_objects.task_title import TaskTitle
    
    title = TaskTitle(value="Buy groceries")
    assert title.value == "Buy groceries"


def test_task_title_strips_whitespace() -> None:
    """Test TaskTitle strips leading/trailing whitespace."""
    from todo_app.domain.value_objects.task_title import TaskTitle
    
    title = TaskTitle(value="  Buy groceries  ")
    assert title.value == "Buy groceries"


def test_task_title_empty_invalid() -> None:
    """Test TaskTitle rejects empty string."""
    from todo_app.domain.value_objects.task_title import TaskTitle
    
    with pytest.raises(ValidationError) as exc_info:
        TaskTitle(value="")
    
    assert "empty" in str(exc_info.value).lower()


def test_task_title_whitespace_only_invalid() -> None:
    """Test TaskTitle rejects whitespace-only string."""
    from todo_app.domain.value_objects.task_title import TaskTitle
    
    with pytest.raises(ValidationError) as exc_info:
        TaskTitle(value="   ")
    
    assert "empty" in str(exc_info.value).lower() or "whitespace" in str(exc_info.value).lower()


def test_task_title_too_long_invalid() -> None:
    """Test TaskTitle rejects strings over 100 characters."""
    from todo_app.domain.value_objects.task_title import TaskTitle
    
    long_title = "x" * 101
    
    with pytest.raises(ValidationError) as exc_info:
        TaskTitle(value=long_title)
    
    assert "100" in str(exc_info.value)


def test_task_title_exactly_100_chars_valid() -> None:
    """Test TaskTitle accepts exactly 100 characters."""
    from todo_app.domain.value_objects.task_title import TaskTitle
    
    title_100 = "x" * 100
    title = TaskTitle(value=title_100)
    assert len(title.value) == 100


def test_task_title_immutable() -> None:
    """Test TaskTitle is immutable (frozen)."""
    from todo_app.domain.value_objects.task_title import TaskTitle
    
    title = TaskTitle(value="Buy groceries")
    
    with pytest.raises((ValidationError, AttributeError)):
        title.value = "New title"  # type: ignore
