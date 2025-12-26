# Data Model: Phase I CLI Todo App

**Feature**: 001-cli-todo  
**Date**: 2025-12-26  
**Status**: Complete

## Overview

This document defines all entities, value objects, and their relationships for the Phase I CLI Todo application following Clean Architecture and Domain-Driven Design principles.

---

## Domain Model Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                       Task (Entity)                          │
├─────────────────────────────────────────────────────────────┤
│ - id: TaskId                                                 │
│ - title: TaskTitle                                           │
│ - description: TaskDescription                               │
│ - status: TaskStatus                                         │
│ - created_at: datetime                                       │
├─────────────────────────────────────────────────────────────┤
│ + toggle_status() -> None                                    │
│ + update_title(title: TaskTitle) -> None                     │
│ + update_description(desc: TaskDescription) -> None          │
│ + is_complete() -> bool                                      │
│ + is_pending() -> bool                                       │
└─────────────────────────────────────────────────────────────┘
         ↓ contains                ↓ contains
    ┌────────┴──────┐         ┌───────┴────────┐
    │   TaskTitle   │         │ TaskDescription │
    │ (Value Object)│         │  (Value Object) │
    └───────────────┘         └─────────────────┘
```

---

## Entities

### Task

**Description**: Represents a todo item with unique identity and lifecycle.

**Attributes**:

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `TaskId` | Required, unique, auto-assigned | Unique identifier for the task |
| `title` | `TaskTitle` | Required, 1-100 chars | Short description of the task |
| `description` | `TaskDescription` | Optional, 0-500 chars | Detailed description |
| `status` | `TaskStatus` | Required, enum | Current completion status |
| `created_at` | `datetime` | Required, auto-set | Timestamp when task was created |

**Business Rules**:
1. Task ID is immutable once assigned
2. Task must always have a valid title (cannot be set to empty)
3. Status can only be PENDING or COMPLETE (no other states)
4. Created timestamp is set once and never modified
5. Title and description can be updated at any time
6. Status can toggle between PENDING and COMPLETE unlimited times

**Business Methods**:

```python
def toggle_status(self) -> None:
    """Toggle task between PENDING and COMPLETE states."""
    if self.status == TaskStatus.PENDING:
        self.status = TaskStatus.COMPLETE
    else:
        self.status = TaskStatus.PENDING

def update_title(self, new_title: TaskTitle) -> None:
    """Update task title with validation."""
    self.title = new_title

def update_description(self, new_description: TaskDescription) -> None:
    """Update task description with validation."""
    self.description = new_description

def is_complete(self) -> bool:
    """Check if task is marked as complete."""
    return self.status == TaskStatus.COMPLETE

def is_pending(self) -> bool:
    """Check if task is pending completion."""
    return self.status == TaskStatus.PENDING
```

**Invariants**:
- Task always has a valid title (enforced by TaskTitle value object)
- Task always has a valid status (enforced by TaskStatus enum)
- Created timestamp is always in the past or present

**Example**:
```python
task = Task(
    id=TaskId(1),
    title=TaskTitle("Buy groceries"),
    description=TaskDescription("Milk, eggs, bread"),
    status=TaskStatus.PENDING,
    created_at=datetime.now()
)
task.toggle_status()  # Now COMPLETE
assert task.is_complete() == True
```

---

## Value Objects

### TaskId

**Description**: Type-safe wrapper for task identifier ensuring valid ID values.

**Attributes**:

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `value` | `int` | > 0 | Positive integer identifier |

**Validation Rules**:
1. Must be a positive integer (> 0)
2. Immutable once created (frozen Pydantic model)
3. Compared by value equality

**Example**:
```python
task_id = TaskId(value=1)
# task_id.value = 2  # Raises error - frozen model
assert task_id == TaskId(value=1)  # Value equality
```

---

### TaskTitle

**Description**: Validated task title ensuring length and content constraints.

**Attributes**:

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `value` | `str` | 1-100 chars, non-empty | The title text |

**Validation Rules**:
1. Minimum length: 1 character
2. Maximum length: 100 characters
3. Cannot be only whitespace
4. Leading/trailing whitespace automatically stripped
5. Immutable once created

**Validation Logic**:
```python
@field_validator('value')
def validate_not_empty(cls, v: str) -> str:
    """Ensure title is not empty or only whitespace."""
    stripped = v.strip()
    if not stripped:
        raise ValueError("Title cannot be empty or only whitespace")
    return stripped

@field_validator('value')
def validate_length(cls, v: str) -> str:
    """Ensure title is within length constraints."""
    if len(v) > 100:
        raise ValueError(f"Title cannot exceed 100 characters (got {len(v)})")
    return v
```

**Example**:
```python
title = TaskTitle(value="Buy groceries")  # Valid
# TaskTitle(value="")  # Raises ValueError
# TaskTitle(value="x" * 101)  # Raises ValueError
```

---

### TaskDescription

**Description**: Optional validated description with length constraints.

**Attributes**:

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `value` | `str` | 0-500 chars, optional | The description text |

**Validation Rules**:
1. Maximum length: 500 characters
2. Empty string is allowed (represents no description)
3. Leading/trailing whitespace automatically stripped
4. Immutable once created

**Validation Logic**:
```python
@field_validator('value')
def validate_length(cls, v: str) -> str:
    """Ensure description does not exceed maximum length."""
    if len(v) > 500:
        raise ValueError(f"Description cannot exceed 500 characters (got {len(v)})")
    return v.strip()
```

**Example**:
```python
desc = TaskDescription(value="Milk, eggs, bread, cheese")  # Valid
desc_empty = TaskDescription(value="")  # Valid - no description
# TaskDescription(value="x" * 501)  # Raises ValueError
```

---

## Enumerations

### TaskStatus

**Description**: Enumeration representing the completion state of a task.

**Values**:

| Value | Description | Display Symbol |
|-------|-------------|----------------|
| `PENDING` | Task not yet completed | ○ (white circle) |
| `COMPLETE` | Task marked as done | ✓ (check mark) |

**Business Rules**:
1. Tasks start as PENDING by default
2. Can toggle between PENDING and COMPLETE
3. No other states allowed (no "in_progress", "blocked", etc. in Phase I)

**Usage**:
```python
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    COMPLETE = "complete"
    
    def symbol(self) -> str:
        """Return display symbol for status."""
        return "✓" if self == TaskStatus.COMPLETE else "○"
    
    def color(self) -> str:
        """Return Rich color code for status."""
        return "green" if self == TaskStatus.COMPLETE else "yellow"
```

---

## Data Transfer Objects (DTOs)

### TaskDTO

**Description**: Serializable representation of Task for transport across layers.

**Purpose**: Decouple domain entities from infrastructure concerns (JSON, CLI output).

**Attributes**:

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `int` | Positive integer | Task identifier |
| `title` | `str` | 1-100 chars | Task title |
| `description` | `str` | 0-500 chars | Task description |
| `status` | `str` | "pending" or "complete" | Status as string |
| `created_at` | `str` | ISO 8601 format | Creation timestamp |

**Conversion Methods**:
```python
@classmethod
def from_entity(cls, task: Task) -> TaskDTO:
    """Convert domain Task entity to DTO."""
    return cls(
        id=task.id.value,
        title=task.title.value,
        description=task.description.value,
        status=task.status.value,
        created_at=task.created_at.isoformat()
    )

def to_entity(self) -> Task:
    """Convert DTO to domain Task entity."""
    return Task(
        id=TaskId(value=self.id),
        title=TaskTitle(value=self.title),
        description=TaskDescription(value=self.description),
        status=TaskStatus(self.status),
        created_at=datetime.fromisoformat(self.created_at)
    )
```

---

### TaskFilter

**Description**: Criteria for filtering task lists.

**Attributes**:

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `status` | `Optional[TaskStatus]` | None or enum value | Filter by status (None = all) |

**Usage**:
```python
filter_all = TaskFilter(status=None)  # Return all tasks
filter_pending = TaskFilter(status=TaskStatus.PENDING)  # Only pending
filter_complete = TaskFilter(status=TaskStatus.COMPLETE)  # Only complete
```

---

## Repository Interface

### TaskRepository (Abstract)

**Description**: Interface defining persistence operations for Task entities.

**Methods**:

```python
from abc import ABC, abstractmethod
from typing import Optional

class TaskRepository(ABC):
    
    @abstractmethod
    def add(self, task: Task) -> Task:
        """
        Add a new task to the repository.
        
        Args:
            task: Task entity (ID may be None/unassigned)
            
        Returns:
            Task with assigned ID
            
        Raises:
            RepositoryError: If add operation fails
        """
        pass
    
    @abstractmethod
    def get_by_id(self, task_id: TaskId) -> Optional[Task]:
        """
        Retrieve task by ID.
        
        Args:
            task_id: The task identifier
            
        Returns:
            Task entity if found, None otherwise
        """
        pass
    
    @abstractmethod
    def get_all(self, filter: Optional[TaskFilter] = None) -> list[Task]:
        """
        Retrieve all tasks, optionally filtered.
        
        Args:
            filter: Optional filter criteria
            
        Returns:
            List of Task entities matching filter
        """
        pass
    
    @abstractmethod
    def update(self, task: Task) -> None:
        """
        Update existing task.
        
        Args:
            task: Task entity with updated values
            
        Raises:
            TaskNotFoundError: If task ID doesn't exist
            RepositoryError: If update operation fails
        """
        pass
    
    @abstractmethod
    def delete(self, task_id: TaskId) -> None:
        """
        Delete task by ID.
        
        Args:
            task_id: The task identifier
            
        Raises:
            TaskNotFoundError: If task ID doesn't exist
            RepositoryError: If delete operation fails
        """
        pass
    
    @abstractmethod
    def count(self, status: Optional[TaskStatus] = None) -> int:
        """
        Count tasks, optionally filtered by status.
        
        Args:
            status: Optional status filter
            
        Returns:
            Number of matching tasks
        """
        pass
```

---

## Aggregate Rules

**Single Aggregate**: Task is the only aggregate root in Phase I.

**Aggregate Boundaries**:
- Task owns its value objects (TaskTitle, TaskDescription)
- Task controls all state changes (toggle, update)
- No task-to-task relationships in Phase I
- Repository operates on complete Task aggregates

**Consistency Rules**:
- All validation happens within the Task aggregate
- Repository ensures ID uniqueness
- No partial updates (always full aggregate)

---

## State Transitions

### Task Status Lifecycle

```
    ┌─────────┐
    │ PENDING │ ←──────┐
    └────┬────┘        │
         │             │
         │ toggle()    │ toggle()
         │             │
         ↓             │
    ┌─────────┐       │
    │COMPLETE │ ──────┘
    └─────────┘
```

**Allowed Transitions**:
1. PENDING → COMPLETE (via `toggle_status()`)
2. COMPLETE → PENDING (via `toggle_status()`)

**Disallowed Transitions**:
- No transition to "deleted" state (delete removes from repository)
- No "in_progress" or intermediate states

---

## Validation Summary

### Domain Layer Validation

| Entity/Value Object | Validation Rules | Enforced By |
|---------------------|------------------|-------------|
| TaskId | value > 0 | Pydantic field validator |
| TaskTitle | 1-100 chars, non-whitespace | Pydantic field validator |
| TaskDescription | 0-500 chars | Pydantic field validator |
| TaskStatus | Must be enum member | Python Enum type |
| Task | All value objects valid | Composition of validated objects |

### Application Layer Validation

| Use Case | Additional Validation | Enforced By |
|----------|----------------------|-------------|
| AddTask | Task doesn't already exist | Use case logic |
| UpdateTask | Task exists before update | Use case logic |
| DeleteTask | Task exists before delete | Use case logic |
| ToggleTask | Task exists before toggle | Use case logic |

---

## Phase I Scope Boundaries

**In Scope**:
- Single Task entity with basic attributes
- Status enumeration (PENDING, COMPLETE)
- Value objects for validation
- Repository interface for persistence abstraction

**Out of Scope** (Future Phases):
- Task priorities (Phase II)
- Due dates and reminders (Phase II)
- Task categories/tags (Phase II)
- Subtasks or task hierarchies (Phase III)
- Task relationships (dependencies) (Phase III)
- Multi-user task assignment (Phase III)

---

## Implementation Checklist

- ✅ Task entity defined with business rules
- ✅ Value objects (TaskId, TaskTitle, TaskDescription) specified
- ✅ TaskStatus enumeration designed
- ✅ DTOs for transport layer defined
- ✅ Repository interface established
- ✅ Validation rules documented
- ✅ State transitions mapped
- ✅ Aggregate boundaries clarified
- ✅ Phase I scope defined

**Status**: Ready for contract generation (Phase 1 completion)
