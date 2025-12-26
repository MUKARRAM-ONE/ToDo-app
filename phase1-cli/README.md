# Phase I: Todo In-Memory Console App

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A beautiful command-line todo application built with Spec-Driven Development using Claude Code and Spec-Kit Plus.

## 🌟 Features

### Basic Level (All Implemented)
- ✅ **Add Task** - Create new todo items with title and description
- ✅ **Delete Task** - Remove tasks from the list with confirmation
- ✅ **Update Task** - Modify existing task details
- ✅ **View Task List** - Display all tasks in beautiful tables with filtering
- ✅ **Mark as Complete** - Toggle task completion status

### User Experience
- 🎨 Beautiful console output with Rich library
- 🎯 Color-coded status indicators (○ pending, ✓ complete)
- 📊 Formatted tables with proper spacing
- ✅ Input validation with helpful error messages
- ⚡ Fast in-memory storage (< 100ms operations)

## 📋 Requirements

- Python 3.13+
- UV (recommended) or pip for dependency management

## 🚀 Quick Start

### Installation

```bash
# Navigate to the phase1-cli directory
cd phase1-cli

# Install dependencies (choose one method)
# Method 1: Using UV (recommended)
uv sync

# Method 2: Using pip
pip install -e .
```

### Interactive Demo

Run the interactive demo to see all features in action:

```bash
python scripts\interactive_demo.py
```

This demonstrates all 5 core features with tasks persisting throughout the session.

## 💻 Usage

### Interactive Mode (User-Friendly)

**Best for:** Regular use, exploring features, continuous task management

```bash
# Start interactive mode
python -m todo_app.interactive

# OR use launcher script
# Windows:
run_todo.bat

# Linux/Mac:
./run_todo.sh
```

**In interactive mode you can:**
- Add multiple tasks in one session
- View tasks with filtering (all/pending/complete)
- Mark tasks as complete with visual confirmation
- Update task details with current value preview
- Delete tasks with confirmation prompts
- Search tasks by keywords
- All tasks persist during your session!

---

### CLI Mode (For Scripting)

**Best for:** Automation, single commands, scripting

```bash
# View help
python -m todo_app --help

# Add a new task
python -m todo_app add "Buy groceries" -d "Milk, eggs, bread"

# List all tasks
python -m todo_app list

# List only pending tasks
python -m todo_app list --filter pending

# List only complete tasks
python -m todo_app list --filter complete

# Toggle task status (complete/pending)
python -m todo_app toggle 1

# Update task
python -m todo_app update 1 --title "Buy groceries and fruits"
python -m todo_app update 1 --description "Updated description"

# Delete task (with confirmation)
python -m todo_app delete 1

# Delete task (skip confirmation)
python -m todo_app delete 1 --yes
```

### Python API

You can also use the application programmatically:

```python
from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
from todo_app.application.use_cases.add_task import AddTaskUseCase
from todo_app.application.use_cases.list_tasks import ListTasksUseCase

# Create repository
repo = InMemoryTaskRepository()

# Add tasks
add_use_case = AddTaskUseCase(repo)
task = add_use_case.execute("Buy groceries", "Milk, eggs, bread")

# List tasks
list_use_case = ListTasksUseCase(repo)
tasks = list_use_case.execute("all")
```

## 🏗️ Architecture

This project follows **Clean Architecture** principles with strict layer separation:

```
src/todo_app/
├── domain/              # Enterprise Business Rules
│   ├── entities/        # Core business entities (Task)
│   ├── value_objects/   # Immutable value objects (TaskId, TaskTitle, etc.)
│   ├── enums/           # Domain enumerations (TaskStatus)
│   └── exceptions.py    # Domain-specific exceptions
│
├── application/         # Application Business Rules
│   ├── use_cases/       # Use case implementations
│   ├── dto/             # Data Transfer Objects
│   ├── interfaces/      # Repository interfaces
│   └── exceptions.py    # Application-specific exceptions
│
└── infrastructure/      # Frameworks & Drivers
    ├── persistence/     # Repository implementations
    ├── cli/             # Command-line interface
    └── config/          # Configuration management
```

### Key Design Patterns

- **Repository Pattern**: Abstraction for data persistence
- **Use Case Pattern**: Single responsibility business logic
- **Value Objects**: Immutable, validated domain primitives
- **DTO Pattern**: Clean layer-to-layer data transfer
- **Dependency Injection**: Loose coupling between layers

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=todo_app --cov-report=html

# Run specific test file
pytest tests/test_domain.py

# Run with verbose output
pytest -v
```

## 📦 Project Structure

```
phase1-cli/
├── .specify/                 # Spec-Kit Plus artifacts
│   └── memory/
│       ├── constitution.md   # Project constitution
│       └── intelligence/     # Reusable intelligence
├── history/                  # Prompt History Records
│   └── prompts/
│       └── phase1-cli-todo/
├── specs/                    # Feature specifications
│   └── 001-cli-todo/
│       ├── spec.md          # Feature specification
│       ├── plan.md          # Implementation plan
│       └── tasks.md         # Task breakdown
├── src/todo_app/            # Application source code
├── tests/                   # Test suite
├── scripts/                 # Utility scripts
├── pyproject.toml           # Project metadata & dependencies
└── README.md               # This file
```

## 🛠️ Development

### Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type checking
mypy src/

# Run all quality checks
ruff check . && mypy src/ && pytest
```

### Building Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --name todo src/todo_app/__main__.py

# Find executable in dist/ folder
```

## 🔧 Technology Stack

- **Python 3.13+** - Modern Python with latest features
- **UV** - Fast Python package manager
- **Click** - Command-line interface framework
- **Rich** - Beautiful console output
- **Pydantic** - Data validation and settings management
- **Pytest** - Testing framework
- **Mypy** - Static type checking
- **Ruff** - Fast Python linter and formatter

## 📝 Important Notes

### In-Memory Storage

**This is a Phase I application with in-memory storage.** Tasks do NOT persist between different command invocations. Each `python -m todo_app` command starts with a fresh, empty repository.

**This is expected behavior** for Phase I requirements.

To work with persistent tasks:
1. Use the **interactive demo** script (`scripts\interactive_demo.py`)
2. Use the **Python API** directly in your own script
3. Wait for **Phase II** which will include database persistence

### Version Control

This project uses:
- **Semantic Versioning** (v1.0.0)
- **Git branching** for features
- **Conventional Commits** for clear history

## 📚 Documentation

- **Constitution**: `.specify/memory/constitution.md` - Project principles and standards
- **Specification**: `specs/001-cli-todo/spec.md` - Complete feature specification
- **Implementation Plan**: `specs/001-cli-todo/plan.md` - Technical design decisions
- **Tasks**: `specs/001-cli-todo/tasks.md` - Detailed task breakdown
- **CLAUDE.md**: `CLAUDE.md` - AI interaction guidelines

## 🎯 Acceptance Criteria

- [x] Can add tasks with title and optional description
- [x] Can view all tasks in formatted table
- [x] Can filter tasks by status (all/pending/complete)
- [x] Can update task title and description
- [x] Can delete tasks with confirmation prompt
- [x] Can mark tasks as complete/incomplete
- [x] All inputs are validated with clear error messages
- [x] Beautiful console output with color coding
- [x] Clean architecture with proper layer separation
- [x] Comprehensive test coverage
- [x] Type hints and linting pass
- [x] Complete documentation

## 🚧 Future Enhancements (Phase II+)

- [ ] Database persistence (PostgreSQL/SQLite)
- [ ] Due dates and priorities
- [ ] Tags and categories
- [ ] Search functionality
- [ ] Web interface (Next.js + FastAPI)
- [ ] AI-powered chatbot
- [ ] Cloud deployment

## 📄 License

This project is part of the "Evolution of Todo" Hackathon II.

## 🙏 Acknowledgments

Built with:
- **Claude Code** - AI-assisted development
- **Spec-Kit Plus** - Spec-Driven Development framework
- **Agentic Dev Stack** - Modern development methodology

---

**Phase**: I - Console Application  
**Status**: ✅ Complete  
**Next**: Phase II - Full-Stack Web Application

# Update task
todo update 1 -t "Buy groceries and pharmacy items"
todo update 1 -d "Updated description"

# Delete task
todo delete 1
todo delete 1 -y  # Skip confirmation
```

## Development

### Setup

```bash
# Install dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests with coverage
pytest

# Run specific test category
pytest tests/unit
pytest tests/integration
pytest tests/acceptance

# Generate HTML coverage report
pytest --cov=todo_app --cov-report=html
```

### Code Quality

```bash
# Lint and format
ruff check .
ruff format .

# Type checking
mypy src/todo_app
```

### Building Executable

```bash
# Windows
.\scripts\build.ps1

# Unix
./scripts/build.sh
```

## Architecture

Built using Clean Architecture principles with three layers:

- **Domain Layer**: Business logic, entities, value objects
- **Application Layer**: Use cases and interfaces
- **Infrastructure Layer**: CLI commands, persistence, formatters

## Requirements

- Python 3.13 or higher
- Dependencies: click, rich, pydantic
- Dev dependencies: pytest, mypy, ruff

## License

MIT License - See LICENSE file for details

## Version

Current version: 0.1.0
