"""Tests for Task entity."""

import pytest
from datetime import datetime
from pydantic import ValidationError


def test_task_creation() -> None:
    """Test creating a valid task."""
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Buy groceries"),
        description=TaskDescription(value="Milk, eggs, bread"),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    assert task.id.value == 1
    assert task.title.value == "Buy groceries"
    assert task.description.value == "Milk, eggs, bread"
    assert task.status == TaskStatus.PENDING


def test_task_toggle_status_pending_to_complete() -> None:
    """Test toggling task from PENDING to COMPLETE."""
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Test task"),
        description=TaskDescription(value=""),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    task.toggle_status()
    assert task.status == TaskStatus.COMPLETE


def test_task_toggle_status_complete_to_pending() -> None:
    """Test toggling task from COMPLETE to PENDING."""
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Test task"),
        description=TaskDescription(value=""),
        status=TaskStatus.COMPLETE,
        created_at=datetime.now()
    )
    
    task.toggle_status()
    assert task.status == TaskStatus.PENDING


def test_task_is_complete() -> None:
    """Test is_complete() method."""
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Test task"),
        description=TaskDescription(value=""),
        status=TaskStatus.COMPLETE,
        created_at=datetime.now()
    )
    
    assert task.is_complete() is True
    assert task.is_pending() is False


def test_task_is_pending() -> None:
    """Test is_pending() method."""
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Test task"),
        description=TaskDescription(value=""),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    assert task.is_pending() is True
    assert task.is_complete() is False


def test_task_update_title() -> None:
    """Test updating task title."""
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Old title"),
        description=TaskDescription(value=""),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    new_title = TaskTitle(value="New title")
    task.update_title(new_title)
    
    assert task.title.value == "New title"


def test_task_update_description() -> None:
    """Test updating task description."""
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Test task"),
        description=TaskDescription(value="Old description"),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    new_desc = TaskDescription(value="New description")
    task.update_description(new_desc)
    
    assert task.description.value == "New description"
