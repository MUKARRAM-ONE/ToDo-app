"""Tests for TaskStatus enum."""

import pytest


def test_task_status_enum_values() -> None:
    """Test TaskStatus has correct enum values."""
    from todo_app.domain.enums.task_status import TaskStatus
    
    assert TaskStatus.PENDING.value == "pending"
    assert TaskStatus.COMPLETE.value == "complete"


def test_task_status_symbol_pending() -> None:
    """Test TaskStatus.PENDING has correct symbol."""
    from todo_app.domain.enums.task_status import TaskStatus
    
    assert TaskStatus.PENDING.symbol() == "○"


def test_task_status_symbol_complete() -> None:
    """Test TaskStatus.COMPLETE has correct symbol."""
    from todo_app.domain.enums.task_status import TaskStatus
    
    assert TaskStatus.COMPLETE.symbol() == "✓"


def test_task_status_color_pending() -> None:
    """Test TaskStatus.PENDING has correct color."""
    from todo_app.domain.enums.task_status import TaskStatus
    
    assert TaskStatus.PENDING.color() == "yellow"


def test_task_status_color_complete() -> None:
    """Test TaskStatus.COMPLETE has correct color."""
    from todo_app.domain.enums.task_status import TaskStatus
    
    assert TaskStatus.COMPLETE.color() == "green"


def test_task_status_equality() -> None:
    """Test TaskStatus enum equality."""
    from todo_app.domain.enums.task_status import TaskStatus
    
    status1 = TaskStatus.PENDING
    status2 = TaskStatus.PENDING
    status3 = TaskStatus.COMPLETE
    
    assert status1 == status2
    assert status1 != status3
