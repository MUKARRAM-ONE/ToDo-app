"""Tests for InMemoryTaskRepository."""

import pytest
from datetime import datetime


def test_repository_add_task() -> None:
    """Test adding a task to repository."""
    from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    repo = InMemoryTaskRepository()
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Test task"),
        description=TaskDescription(value=""),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    added_task = repo.add(task)
    
    assert added_task.id.value == 1
    assert added_task.title.value == "Test task"


def test_repository_get_by_id() -> None:
    """Test retrieving task by ID."""
    from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    repo = InMemoryTaskRepository()
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Test task"),
        description=TaskDescription(value=""),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    repo.add(task)
    
    retrieved = repo.get_by_id(TaskId(value=1))
    
    assert retrieved is not None
    assert retrieved.title.value == "Test task"


def test_repository_get_by_id_not_found() -> None:
    """Test retrieving non-existent task returns None."""
    from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
    from todo_app.domain.value_objects.task_id import TaskId
    
    repo = InMemoryTaskRepository()
    
    retrieved = repo.get_by_id(TaskId(value=999))
    
    assert retrieved is None


def test_repository_get_all() -> None:
    """Test retrieving all tasks."""
    from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    repo = InMemoryTaskRepository()
    
    task1 = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Task 1"),
        description=TaskDescription(value=""),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    task2 = Task(
        id=TaskId(value=2),
        title=TaskTitle(value="Task 2"),
        description=TaskDescription(value=""),
        status=TaskStatus.COMPLETE,
        created_at=datetime.now()
    )
    
    repo.add(task1)
    repo.add(task2)
    
    all_tasks = repo.get_all()
    
    assert len(all_tasks) == 2


def test_repository_update_task() -> None:
    """Test updating a task."""
    from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    repo = InMemoryTaskRepository()
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Original"),
        description=TaskDescription(value=""),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    repo.add(task)
    
    task.update_title(TaskTitle(value="Updated"))
    repo.update(task)
    
    retrieved = repo.get_by_id(TaskId(value=1))
    
    assert retrieved is not None
    assert retrieved.title.value == "Updated"


def test_repository_delete_task() -> None:
    """Test deleting a task."""
    from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    repo = InMemoryTaskRepository()
    
    task = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Test task"),
        description=TaskDescription(value=""),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    repo.add(task)
    repo.delete(TaskId(value=1))
    
    retrieved = repo.get_by_id(TaskId(value=1))
    
    assert retrieved is None


def test_repository_count() -> None:
    """Test counting tasks."""
    from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
    from todo_app.domain.entities.task import Task
    from todo_app.domain.value_objects.task_id import TaskId
    from todo_app.domain.value_objects.task_title import TaskTitle
    from todo_app.domain.value_objects.task_description import TaskDescription
    from todo_app.domain.enums.task_status import TaskStatus
    
    repo = InMemoryTaskRepository()
    
    task1 = Task(
        id=TaskId(value=1),
        title=TaskTitle(value="Task 1"),
        description=TaskDescription(value=""),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    task2 = Task(
        id=TaskId(value=2),
        title=TaskTitle(value="Task 2"),
        description=TaskDescription(value=""),
        status=TaskStatus.COMPLETE,
        created_at=datetime.now()
    )
    
    repo.add(task1)
    repo.add(task2)
    
    count = repo.count()
    
    assert count == 2
