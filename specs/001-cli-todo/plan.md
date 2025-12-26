# Implementation Plan: Phase I CLI Todo App

**Branch**: `001-cli-todo` | **Date**: 2025-12-26 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-cli-todo/spec.md`

## Summary

Build an in-memory command-line todo application using Clean Architecture principles with three distinct layers: domain (core business logic), application (use cases), and infrastructure (CLI interface). The application will use Python 3.13+ with modern practices including Pydantic for validation, Rich for beautiful console output, and comprehensive pytest-based testing achieving >90% coverage. Development follows strict Test-Driven Development with the Red-Green-Refactor cycle, ensuring all functionality is validated before implementation. The deliverable is a standalone executable created with PyInstaller/Inno Setup that provides add, list, toggle, update, and delete operations for managing tasks in memory.

## Technical Context

**Language/Version**: Python 3.13+  
**Primary Dependencies**: 
  - Pydantic 2.x (data validation, models)
  - Rich 13.x (console UI, tables, formatting)
  - Click 8.x (CLI framework, command routing)
  - pytest 8.x (testing framework)
  - pytest-cov 4.x (coverage reporting)
  - ruff (linting, formatting)
  - mypy (static type checking)
  - PyInstaller (executable generation)

**Storage**: In-memory (Python dict/list structures)  
**Testing**: pytest with fixtures, parametrization, and >90% coverage target  
**Target Platform**: Windows 10/11 (primary), cross-platform compatible (Linux, macOS)  
**Project Type**: Single project (CLI application)  
**Performance Goals**: 
  - Operation completion <100ms for up to 1000 tasks
  - Startup time <1 second
  - Memory usage <50MB for 1000 tasks

**Constraints**: 
  - No persistence between sessions (in-memory only)
  - Single-user, single-process execution
  - Console-based interface only
  - Must be distributable as standalone executable
  - No external service dependencies

**Scale/Scope**: 
  - Support 1000 tasks in memory without degradation
  - 5 primary commands (add, list, toggle, update, delete)
  - ~15-20 source files across 3 architectural layers
  - Target 90%+ test coverage

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence/Notes |
|-----------|--------|----------------|
| **I. Spec-First Development** | ✅ PASS | Complete spec.md exists with user scenarios, acceptance criteria, functional requirements, and success criteria before implementation |
| **II. AI-Assisted Implementation** | ✅ PASS | Plan designed for Claude Code execution with clear architectural decisions and task breakdown |
| **III. Test-Driven Development** | ✅ PASS | Red-Green-Refactor cycle planned with pytest, >90% coverage target, 100% critical path coverage (domain + application layers) |
| **IV. Clean Architecture** | ✅ PASS | Three-layer separation: Domain (entities, value objects), Application (use cases), Infrastructure (CLI, repository) with proper dependencies |
| **V. Version Control & Releasability** | ✅ PASS | Branch 001-cli-todo created, semantic versioning planned (0.1.0 → 1.0.0), changelog and release notes in scope |
| **VI. Agile Methodology** | ✅ PASS | Phase-based delivery (Phase 0: Research, Phase 1: Design, Phase 2: Tasks), working software at each milestone, PHR tracking |
| **VII. Zero Manual Boilerplate** | ✅ PASS | Pydantic models generate validation, CLI commands use Click decorators, test fixtures autogenerate, repository patterns templated |
| **VIII. Documentation-Driven** | ✅ PASS | Type hints required, docstrings for public APIs, README with setup/usage, ADRs for significant choices, PHRs for process tracking |

**Quality Gates Status**:
- ✅ Code Quality: ruff + mypy strict mode configured
- ✅ Testing: pytest with >90% coverage requirement
- ✅ Configuration: No hardcoded values, environment/config pattern
- ✅ Error Handling: Pydantic validation, custom exceptions, user-friendly messages
- ✅ Observability: Structured logging planned

**Technology Constraints Compliance**:
- ✅ Python 3.13+ (verified in pyproject.toml)
- ✅ UV for dependency management (project standard)
- ✅ Pydantic for validation
- ✅ Rich for console formatting
- ✅ pytest for testing
- ✅ ruff + mypy for code quality
- ✅ Inno Setup for Windows distribution

**Overall**: All constitutional requirements satisfied. No violations requiring justification.

## Project Structure

### Documentation (this feature)

```text
specs/001-cli-todo/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── cli-commands.yaml # CLI command specifications
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
phase1-cli/
├── src/
│   ├── todo_app/
│   │   ├── __init__.py
│   │   ├── domain/              # Domain Layer (Pure Business Logic)
│   │   │   ├── __init__.py
│   │   │   ├── entities/
│   │   │   │   ├── __init__.py
│   │   │   │   └── task.py      # Task entity with business rules
│   │   │   ├── value_objects/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── task_id.py   # Type-safe task ID
│   │   │   │   ├── task_title.py # Validated title (1-100 chars)
│   │   │   │   └── task_description.py # Validated description (0-500 chars)
│   │   │   ├── enums/
│   │   │   │   ├── __init__.py
│   │   │   │   └── task_status.py # TaskStatus enum (PENDING, COMPLETE)
│   │   │   └── exceptions.py    # Domain-specific exceptions
│   │   ├── application/         # Application Layer (Use Cases)
│   │   │   ├── __init__.py
│   │   │   ├── interfaces/
│   │   │   │   ├── __init__.py
│   │   │   │   └── task_repository.py # Repository interface (abstract)
│   │   │   ├── use_cases/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── add_task.py  # AddTaskUseCase
│   │   │   │   ├── list_tasks.py # ListTasksUseCase with filtering
│   │   │   │   ├── toggle_task.py # ToggleTaskUseCase
│   │   │   │   ├── update_task.py # UpdateTaskUseCase
│   │   │   │   └── delete_task.py # DeleteTaskUseCase
│   │   │   ├── dto/             # Data Transfer Objects
│   │   │   │   ├── __init__.py
│   │   │   │   ├── task_dto.py  # Task representation for transport
│   │   │   │   └── task_filter.py # Filter criteria for list operation
│   │   │   └── exceptions.py    # Application-level exceptions
│   │   └── infrastructure/      # Infrastructure Layer (CLI, Persistence)
│   │       ├── __init__.py
│   │       ├── cli/
│   │       │   ├── __init__.py
│   │       │   ├── app.py       # Main Click application entry
│   │       │   ├── commands/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── add.py   # add command handler
│   │       │   │   ├── list.py  # list command handler
│   │       │   │   ├── toggle.py # toggle command handler
│   │       │   │   ├── update.py # update command handler
│   │       │   │   └── delete.py # delete command handler
│   │       │   ├── formatters/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── table_formatter.py # Rich table formatting
│   │       │   │   └── message_formatter.py # Status messages, colors
│   │       │   └── validators.py # CLI input validation
│   │       ├── persistence/
│   │       │   ├── __init__.py
│   │       │   └── in_memory_repository.py # In-memory TaskRepository impl
│   │       ├── config/
│   │       │   ├── __init__.py
│   │       │   └── settings.py  # Pydantic settings model
│   │       └── logging/
│   │           ├── __init__.py
│   │           └── logger.py    # Structured logging configuration
│   └── __main__.py              # Entry point for python -m todo_app
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Shared fixtures
│   ├── unit/                    # Fast, isolated unit tests
│   │   ├── __init__.py
│   │   ├── domain/
│   │   │   ├── __init__.py
│   │   │   ├── test_task_entity.py
│   │   │   ├── test_task_title.py
│   │   │   ├── test_task_description.py
│   │   │   ├── test_task_id.py
│   │   │   └── test_task_status.py
│   │   ├── application/
│   │   │   ├── __init__.py
│   │   │   ├── test_add_task_use_case.py
│   │   │   ├── test_list_tasks_use_case.py
│   │   │   ├── test_toggle_task_use_case.py
│   │   │   ├── test_update_task_use_case.py
│   │   │   └── test_delete_task_use_case.py
│   │   └── infrastructure/
│   │       ├── __init__.py
│   │       ├── test_in_memory_repository.py
│   │       ├── test_table_formatter.py
│   │       └── test_message_formatter.py
│   ├── integration/             # Cross-layer integration tests
│   │   ├── __init__.py
│   │   ├── test_add_task_flow.py
│   │   ├── test_list_tasks_flow.py
│   │   ├── test_toggle_task_flow.py
│   │   ├── test_update_task_flow.py
│   │   └── test_delete_task_flow.py
│   └── acceptance/              # User scenario tests (E2E)
│       ├── __init__.py
│       ├── test_user_story_1_add_track.py
│       ├── test_user_story_2_view_list.py
│       ├── test_user_story_3_mark_complete.py
│       ├── test_user_story_4_update_details.py
│       └── test_user_story_5_delete_task.py
│
├── pyproject.toml               # UV/pip configuration, dependencies
├── pytest.ini                   # Pytest configuration
├── mypy.ini                     # MyPy type checking configuration
├── ruff.toml                    # Ruff linting configuration
├── .python-version              # Python version specification (3.13)
├── README.md                    # User-facing documentation
├── CHANGELOG.md                 # Version history
└── scripts/
    ├── build.ps1                # Windows build script (PyInstaller)
    ├── build.sh                 # Unix build script
    ├── setup-installer.iss      # Inno Setup configuration
    └── run-tests.ps1            # Comprehensive test runner
```

**Structure Decision**: Single project structure selected as this is a standalone CLI application. Clean Architecture enforced through three distinct layers:
- **Domain Layer** (`domain/`): Zero external dependencies, pure business logic, entities and value objects
- **Application Layer** (`application/`): Depends only on domain, orchestrates use cases, defines repository interfaces
- **Infrastructure Layer** (`infrastructure/`): Depends on application and domain, implements CLI commands, persistence, and external concerns

This structure supports test-driven development with clear boundaries for unit, integration, and acceptance tests.

## Complexity Tracking

> **No violations requiring justification - all constitutional requirements satisfied**

This implementation adheres to all constitutional principles:
- Clean Architecture maintained with strict layer separation
- TDD enforced through comprehensive test strategy
- AI-assisted implementation via Claude Code with clear specifications
- All quality gates and technology constraints satisfied
- No exceptions or workarounds needed
