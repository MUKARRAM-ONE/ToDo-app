# Research Document: Phase I CLI Todo App

**Feature**: 001-cli-todo  
**Date**: 2025-12-26  
**Status**: Complete

## Overview

This document captures research findings and architectural decisions for the Phase I CLI Todo application, resolving all technical uncertainties and establishing best practices for implementation.

---

## Decision 1: CLI Framework Selection

**Context**: Need to select appropriate CLI framework for Python 3.13+ that supports command routing, argument parsing, and maintainable command structure.

**Decision**: Use Click 8.x as primary CLI framework

**Rationale**:
- **Decorator-based API**: Natural Python syntax with `@click.command()` decorators reduces boilerplate
- **Automatic help generation**: Built-in help text from decorators and docstrings
- **Type validation**: Native support for type conversion and validation
- **Composability**: Command groups support hierarchical command structure for future expansion
- **Testing support**: Click provides `CliRunner` for isolated command testing
- **Active maintenance**: Current stable release, Python 3.13 compatible
- **Rich integration**: Works seamlessly with Rich library for output formatting

**Alternatives Considered**:
- **argparse** (stdlib): Rejected - more verbose, manual help text management, less intuitive API
- **Typer**: Rejected - while modern, Click's maturity and extensive ecosystem better suited for TDD approach
- **Fire**: Rejected - magic behavior makes testing and explicit contracts harder to maintain

**Implementation Impact**: 
- Commands defined as Click command functions with decorators
- Parameters use Click types (`click.INT`, `click.STRING`)
- Integration point: `infrastructure/cli/app.py` creates Click application, command modules register with it

---

## Decision 2: Data Validation Strategy

**Context**: Need robust validation for task title (1-100 chars), description (0-500 chars), and business rules enforcement.

**Decision**: Use Pydantic 2.x for all data validation and modeling

**Rationale**:
- **Type safety**: Integrates with mypy for compile-time validation
- **Validation rules**: Field validators handle length constraints, custom validation logic
- **Performance**: Pydantic V2 uses Rust core, extremely fast validation
- **Error messages**: Automatic generation of detailed, user-friendly validation errors
- **Immutability support**: `frozen=True` for value objects ensures data integrity
- **JSON serialization**: Built-in serialization for future API extensions
- **Settings management**: `BaseSettings` handles configuration with environment variable support

**Alternatives Considered**:
- **Dataclasses + manual validation**: Rejected - requires significant boilerplate, error-prone
- **attrs + validators**: Rejected - less integrated with type system, smaller ecosystem
- **Marshmallow**: Rejected - primarily for API serialization, overkill for CLI validation

**Implementation Impact**:
- Value objects (`TaskTitle`, `TaskDescription`) as frozen Pydantic models with validators
- Entity (`Task`) as Pydantic model with business logic methods
- DTOs in application layer use Pydantic for transport
- Settings configuration via Pydantic `BaseSettings`

**Best Practice Pattern**:
```python
from pydantic import BaseModel, Field, field_validator

class TaskTitle(BaseModel, frozen=True):
    value: str = Field(min_length=1, max_length=100)
    
    @field_validator('value')
    def validate_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty or whitespace only')
        return v.strip()
```

---

## Decision 3: Console UI Library

**Context**: Requirement for "beautiful console interface" with formatted tables, status symbols, and color coding.

**Decision**: Use Rich 13.x for all console output formatting

**Rationale**:
- **Table rendering**: Built-in `Table` class with automatic column sizing, borders, styling
- **Unicode support**: Native rendering of status symbols (○, ✓) across platforms
- **Color/styling**: Semantic color markup with `[green]`, `[red]` syntax
- **Console abstraction**: `Console` object enables testing output without TTY
- **Progress indicators**: Built-in progress bars for future file operations
- **Markdown rendering**: For help text and documentation display
- **Cross-platform**: Handles Windows console limitations gracefully

**Alternatives Considered**:
- **colorama**: Rejected - only color support, no table formatting
- **tabulate**: Rejected - basic tables, no styling or unicode support
- **termcolor**: Rejected - minimal features compared to Rich

**Implementation Impact**:
- `TableFormatter` class wraps Rich `Table` for task list display
- `MessageFormatter` uses Rich `Console` for status messages with colors
- All CLI output goes through Rich abstractions for testability
- Test fixtures mock `Console` to capture and assert on output

**Best Practice Pattern**:
```python
from rich.console import Console
from rich.table import Table

def format_task_list(tasks: list[TaskDTO], console: Console) -> None:
    table = Table(title="Tasks", show_header=True)
    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Status", justify="center")
    table.add_column("Title", style="white")
    
    for task in tasks:
        status_icon = "✓" if task.status == "complete" else "○"
        status_color = "green" if task.status == "complete" else "yellow"
        table.add_row(
            str(task.id),
            f"[{status_color}]{status_icon}[/{status_color}]",
            task.title
        )
    
    console.print(table)
```

---

## Decision 4: In-Memory Repository Pattern

**Context**: Phase I requires in-memory storage with no persistence, but must support future database integration in Phase II.

**Decision**: Implement Repository pattern with in-memory dict-based storage

**Rationale**:
- **Interface segregation**: Abstract `TaskRepository` interface in application layer enables future implementations
- **Testability**: Easy to create mock repositories for use case testing
- **Domain independence**: Domain layer never depends on storage implementation
- **Migration path**: Phase II can add PostgreSQL repository without domain changes
- **Simplicity**: In-memory dict provides O(1) access by task ID
- **Thread safety**: Python dict is thread-safe for single-process CLI app

**Alternatives Considered**:
- **Direct list manipulation**: Rejected - violates Clean Architecture, couples domain to storage
- **SQLite in-memory**: Rejected - unnecessary complexity for Phase I, introduces SQL dependency
- **Pickle/JSON files**: Rejected - out of scope for Phase I (no persistence requirement)

**Implementation Impact**:
- `application/interfaces/task_repository.py` defines abstract repository interface
- `infrastructure/persistence/in_memory_repository.py` implements using `dict[int, Task]`
- Use cases receive repository via dependency injection (constructor parameter)
- ID generation uses simple counter starting at 1

**Best Practice Pattern**:
```python
from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.task import Task

class TaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> Task:
        """Add task and return with assigned ID"""
        pass
    
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve task by ID or None if not found"""
        pass
    
    @abstractmethod
    def get_all(self) -> list[Task]:
        """Retrieve all tasks"""
        pass
    
    @abstractmethod
    def update(self, task: Task) -> None:
        """Update existing task"""
        pass
    
    @abstractmethod
    def delete(self, task_id: int) -> None:
        """Delete task by ID"""
        pass

# Implementation
class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1
    
    def add(self, task: Task) -> Task:
        task.id = self._next_id
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task
```

---

## Decision 5: Error Handling Strategy

**Context**: Need comprehensive error handling for domain violations, validation errors, and user input errors with clear messages.

**Decision**: Layered exception hierarchy with custom exceptions per layer

**Rationale**:
- **Domain exceptions**: Business rule violations (e.g., `InvalidTaskTitleError`)
- **Application exceptions**: Use case failures (e.g., `TaskNotFoundError`)
- **Infrastructure exceptions**: CLI/external errors (e.g., `CommandExecutionError`)
- **Clarity**: Each layer owns its exceptions, no leakage between boundaries
- **User experience**: Infrastructure layer translates exceptions to user-friendly CLI messages
- **Logging**: Exceptions carry context for structured logging

**Alternatives Considered**:
- **Single exception type**: Rejected - loses semantic meaning, harder to handle specifically
- **HTTP-style error codes**: Rejected - unnecessary complexity for CLI application
- **Result types (monads)**: Rejected - not idiomatic Python, complicates implementation

**Implementation Impact**:
- `domain/exceptions.py`: Domain-specific exceptions (validation, business rules)
- `application/exceptions.py`: Application-level exceptions (not found, conflict)
- CLI commands catch exceptions and use Rich to display formatted error messages
- All exceptions inherit from base `TodoAppError` for consistent handling

**Best Practice Pattern**:
```python
# domain/exceptions.py
class TodoAppError(Exception):
    """Base exception for all app errors"""
    pass

class DomainError(TodoAppError):
    """Base for domain layer errors"""
    pass

class InvalidTaskTitleError(DomainError):
    def __init__(self, title: str, reason: str):
        self.title = title
        self.reason = reason
        super().__init__(f"Invalid task title '{title}': {reason}")

# application/exceptions.py
class TaskNotFoundError(TodoAppError):
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task ID {task_id} not found")

# CLI handler
try:
    use_case.execute(task_id)
except TaskNotFoundError as e:
    console.print(f"[red]Error: {e}[/red]")
    raise click.Abort()
```

---

## Decision 6: Testing Strategy

**Context**: Constitutional requirement for TDD with >90% coverage, 100% critical path coverage.

**Decision**: Three-tier testing pyramid with pytest

**Test Layers**:

1. **Unit Tests** (Fast, Isolated)
   - Domain entities, value objects, business logic
   - Application use cases with mocked repositories
   - Infrastructure components (formatters, validators)
   - **Coverage Target**: 100% for domain and application layers
   - **Speed**: <1 second for full suite

2. **Integration Tests** (Cross-Layer)
   - Use cases with real in-memory repository
   - CLI commands end-to-end with Click's CliRunner
   - Formatter integration with Rich console
   - **Coverage Target**: All layer interactions
   - **Speed**: <5 seconds for full suite

3. **Acceptance Tests** (User Scenarios)
   - Each user story from spec.md as executable test
   - Full application workflow with all components
   - Tests acceptance criteria from specification
   - **Coverage Target**: All functional requirements validated
   - **Speed**: <10 seconds for full suite

**Rationale**:
- **Pyramid structure**: More unit tests (fast feedback), fewer integration/acceptance tests (confidence)
- **TDD enablement**: Unit tests written first, guide implementation
- **Regression protection**: Acceptance tests prevent feature breakage
- **Documentation**: Tests serve as living documentation of behavior

**Tools & Patterns**:
- `pytest` with fixtures for dependency injection
- `pytest-cov` for coverage reporting
- `Click.CliRunner` for command testing without subprocess
- Parametrized tests for validation edge cases
- Shared fixtures in `conftest.py`

**Best Practice Pattern**:
```python
# tests/unit/application/test_add_task_use_case.py
import pytest
from unittest.mock import Mock
from application.use_cases.add_task import AddTaskUseCase
from domain.value_objects.task_title import TaskTitle

def test_add_task_success():
    # Arrange
    mock_repo = Mock()
    use_case = AddTaskUseCase(mock_repo)
    title = "Buy groceries"
    
    # Act
    result = use_case.execute(title=title, description=None)
    
    # Assert
    mock_repo.add.assert_called_once()
    assert result.title == title
    assert result.status == "pending"

@pytest.mark.parametrize("invalid_title", ["", "x" * 101])
def test_add_task_invalid_title(invalid_title):
    use_case = AddTaskUseCase(Mock())
    with pytest.raises(InvalidTaskTitleError):
        use_case.execute(title=invalid_title, description=None)
```

---

## Decision 7: Dependency Management & Build

**Context**: Constitutional requirement for UV package manager, executable distribution via PyInstaller/Inno Setup.

**Decision**: UV for dev dependencies, PyInstaller for executable, Inno Setup for Windows installer

**Rationale**:

**UV**:
- Fast dependency resolution (10-100x faster than pip)
- Lock file for reproducible builds
- Virtual environment management
- pip-compatible (uses `pyproject.toml`)

**PyInstaller**:
- Single-file executable generation
- Bundles Python interpreter and dependencies
- Cross-platform (Windows, Linux, macOS)
- No end-user dependencies required

**Inno Setup**:
- Professional Windows installer (MSI-style)
- Desktop shortcuts, Start menu entries
- Uninstall support
- Version upgrade handling

**Alternatives Considered**:
- **Poetry**: Rejected - UV is faster, simpler, constitutional requirement
- **cx_Freeze**: Rejected - less mature than PyInstaller for Python 3.13
- **NSIS**: Rejected - Inno Setup more user-friendly, better documentation

**Implementation Impact**:
- `pyproject.toml`: Define dependencies, versions, project metadata
- `scripts/build.ps1`: Automated build script for Windows (UV install → PyInstaller)
- `scripts/setup-installer.iss`: Inno Setup configuration for installer creation
- CI/CD: Build pipeline uses UV for speed, generates executables as artifacts

**Best Practice Pattern**:
```toml
# pyproject.toml
[project]
name = "todo-app"
version = "1.0.0"
description = "Phase I CLI Todo Application"
requires-python = ">=3.13"
dependencies = [
    "click>=8.1.0",
    "rich>=13.0.0",
    "pydantic>=2.5.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=4.1.0",
    "mypy>=1.8.0",
    "ruff>=0.1.0",
]

[project.scripts]
todo = "todo_app.infrastructure.cli.app:main"
```

**Build Script Pattern**:
```powershell
# scripts/build.ps1
uv pip install -e .
uv pip install pyinstaller

pyinstaller --onefile `
    --name todo-app `
    --add-data "src/todo_app:todo_app" `
    --console `
    src/todo_app/__main__.py

# Output: dist/todo-app.exe
```

---

## Decision 8: Type Safety & Linting

**Context**: Constitutional requirement for mypy strict mode, ruff linting with zero violations.

**Decision**: Comprehensive static analysis with strict configuration

**Configuration**:

**mypy (Type Checking)**:
- Strict mode enabled
- No implicit `Optional`
- Warn on unused ignores
- Check untyped definitions
- Disallow any generics

**ruff (Linting & Formatting)**:
- All default rules enabled
- Line length: 100 characters
- Import sorting (isort-compatible)
- Docstring enforcement (pydocstyle)
- Complexity limits (McCabe)

**Rationale**:
- **Type safety**: Catch errors at development time, not runtime
- **Consistency**: Automated formatting eliminates style debates
- **Quality**: Enforces best practices (unused imports, complexity, etc.)
- **AI-friendly**: Clear type information helps Claude Code generate better code

**Implementation Impact**:
- All functions have type hints including return types
- No `# type: ignore` without justification
- Pre-commit hooks run mypy and ruff before each commit
- CI pipeline fails on any linting or type errors

**Best Practice Pattern**:
```python
# mypy.ini
[mypy]
python_version = 3.13
strict = True
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True

# ruff.toml
[tool.ruff]
line-length = 100
select = ["E", "F", "I", "N", "W", "B", "C90", "D"]
ignore = ["D203", "D213"]  # Conflicting docstring rules

[tool.ruff.per-file-ignores]
"tests/*" = ["D"]  # No docstrings required in tests
```

---

## Summary of Technical Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Language** | Python | 3.13+ | Modern type system, performance |
| **CLI Framework** | Click | 8.x | Command routing, argument parsing |
| **Validation** | Pydantic | 2.x | Data models, validation rules |
| **Console UI** | Rich | 13.x | Tables, colors, formatting |
| **Testing** | pytest | 8.x | Test execution, fixtures |
| **Coverage** | pytest-cov | 4.x | Code coverage reporting |
| **Type Checking** | mypy | 1.8+ | Static type validation |
| **Linting** | ruff | 0.1+ | Code quality, formatting |
| **Package Manager** | UV | latest | Fast dependency management |
| **Executable** | PyInstaller | latest | Standalone binary creation |
| **Installer** | Inno Setup | 6.x | Windows installer generation |

---

## Implementation Readiness Checklist

- ✅ CLI framework selected and rationale documented
- ✅ Validation strategy defined with Pydantic patterns
- ✅ Console UI approach established with Rich
- ✅ Repository pattern designed for future persistence
- ✅ Error handling hierarchy established
- ✅ Testing strategy defined (unit, integration, acceptance)
- ✅ Build and distribution tools selected
- ✅ Type safety and linting configuration specified
- ✅ All constitutional requirements addressed
- ✅ No unresolved technical uncertainties

**Status**: Ready to proceed to Phase 1 (Design & Contracts)
