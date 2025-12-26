"""Tests for TaskDescription value object."""

import pytest
from pydantic import ValidationError


def test_task_description_valid() -> None:
    """Test TaskDescription accepts valid strings."""
    from todo_app.domain.value_objects.task_description import TaskDescription
    
    desc = TaskDescription(value="Milk, eggs, bread")
    assert desc.value == "Milk, eggs, bread"


def test_task_description_empty_valid() -> None:
    """Test TaskDescription accepts empty string."""
    from todo_app.domain.value_objects.task_description import TaskDescription
    
    desc = TaskDescription(value="")
    assert desc.value == ""


def test_task_description_strips_whitespace() -> None:
    """Test TaskDescription strips leading/trailing whitespace."""
    from todo_app.domain.value_objects.task_description import TaskDescription
    
    desc = TaskDescription(value="  Some description  ")
    assert desc.value == "Some description"


def test_task_description_too_long_invalid() -> None:
    """Test TaskDescription rejects strings over 500 characters."""
    from todo_app.domain.value_objects.task_description import TaskDescription
    
    long_desc = "x" * 501
    
    with pytest.raises(ValidationError) as exc_info:
        TaskDescription(value=long_desc)
    
    assert "500" in str(exc_info.value)


def test_task_description_exactly_500_chars_valid() -> None:
    """Test TaskDescription accepts exactly 500 characters."""
    from todo_app.domain.value_objects.task_description import TaskDescription
    
    desc_500 = "x" * 500
    desc = TaskDescription(value=desc_500)
    assert len(desc.value) == 500


def test_task_description_immutable() -> None:
    """Test TaskDescription is immutable (frozen)."""
    from todo_app.domain.value_objects.task_description import TaskDescription
    
    desc = TaskDescription(value="Some description")
    
    with pytest.raises((ValidationError, AttributeError)):
        desc.value = "New description"  # type: ignore
