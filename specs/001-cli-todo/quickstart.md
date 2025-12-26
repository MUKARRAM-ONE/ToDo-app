# Quickstart Guide: Phase I CLI Todo App

**Version**: 1.0.0  
**Date**: 2025-12-26  
**Audience**: Developers implementing the Phase I CLI Todo App

## Overview

This quickstart guide provides step-by-step instructions for setting up the development environment, running tests, building the application, and generating the distributable executable for the Phase I CLI Todo App.

---

## Prerequisites

Before starting, ensure you have:

- **Python 3.13+** installed and available in PATH
- **UV** package manager installed ([installation guide](https://github.com/astral-sh/uv))
- **Git** for version control
- **Windows 10/11** (for Inno Setup installer creation) or Linux/macOS for development
- **Terminal/PowerShell** with UTF-8 encoding support

### Verify Prerequisites

```powershell
# Check Python version
python --version  # Should show Python 3.13.x or higher

# Check UV installation
uv --version  # Should show uv version

# Check Git
git --version
```

---

## Project Setup

### 1. Clone and Navigate to Project

```bash
git clone <repository-url>
cd ToDo-app
git checkout 001-cli-todo
```

### 2. Create Virtual Environment and Install Dependencies

```powershell
# Create virtual environment with UV
uv venv

# Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Or on Unix/macOS
source .venv/bin/activate

# Install project dependencies
cd phase1-cli
uv pip install -e .

# Install development dependencies
uv pip install -e ".[dev]"
```

### 3. Verify Installation

```bash
# Check installed packages
uv pip list

# Verify todo command is available
python -m todo_app --version
```

---

## Development Workflow

### Project Structure Overview

```
phase1-cli/
├── src/todo_app/          # Application source code
│   ├── domain/            # Business logic (entities, value objects)
│   ├── application/       # Use cases and interfaces
│   └── infrastructure/    # CLI, repository, formatters
├── tests/                 # Test suites
│   ├── unit/              # Fast isolated tests
│   ├── integration/       # Cross-layer tests
│   └── acceptance/        # User scenario tests
├── pyproject.toml         # Project configuration
└── scripts/               # Build and utility scripts
```

### Running the Application (Development Mode)

```bash
# Run directly with Python module
python -m todo_app --help

# Or use the installed command (after pip install -e .)
todo --help

# Add a task
python -m todo_app add "My first task" -d "This is a test"

# List all tasks
python -m todo_app list

# Toggle task status
python -m todo_app toggle 1

# Update task
python -m todo_app update 1 -t "Updated title"

# Delete task
python -m todo_app delete 1 -y
```

---

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=todo_app --cov-report=html --cov-report=term

# Run specific test category
pytest tests/unit/            # Unit tests only
pytest tests/integration/     # Integration tests only
pytest tests/acceptance/      # Acceptance tests only

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/unit/domain/test_task_entity.py

# Run tests matching pattern
pytest -k "test_add_task"
```

### Coverage Report

After running tests with coverage:

```bash
# View HTML coverage report
# Windows
start htmlcov/index.html

# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html
```

**Coverage Targets**:
- Overall: >90%
- Domain layer: 100%
- Application layer: 100%
- Infrastructure layer: >80%

---

## Code Quality

### Linting and Formatting

```bash
# Run ruff linter
ruff check .

# Auto-fix issues
ruff check --fix .

# Format code
ruff format .

# Check specific file
ruff check src/todo_app/domain/entities/task.py
```

### Type Checking

```bash
# Run mypy type checker
mypy src/todo_app

# Check specific module
mypy src/todo_app/domain

# Generate type checking report
mypy src/todo_app --html-report mypy-report
```

### Pre-Commit Hooks (Recommended)

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

---

## Building Executable

### Build Standalone Executable (PyInstaller)

```powershell
# Run build script (Windows)
.\scripts\build.ps1

# Or build manually
pyinstaller --onefile `
    --name todo-app `
    --add-data "src/todo_app:todo_app" `
    --console `
    src/todo_app/__main__.py

# Output: dist/todo-app.exe (Windows) or dist/todo-app (Unix)
```

### Test Executable

```bash
# Run the built executable
.\dist\todo-app.exe --help  # Windows
./dist/todo-app --help      # Unix

# Test basic functionality
.\dist\todo-app.exe add "Test task"
.\dist\todo-app.exe list
```

---

## Creating Windows Installer (Inno Setup)

### Prerequisites

- Install **Inno Setup 6.x** from [jrsoftware.org](https://jrsoftware.org/isinfo.php)

### Build Installer

```powershell
# Ensure executable is built first
.\scripts\build.ps1

# Compile installer with Inno Setup
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" scripts\setup-installer.iss

# Output: Output/todo-app-setup.exe
```

### Test Installer

1. Run `Output/todo-app-setup.exe`
2. Follow installation wizard
3. Verify Start Menu shortcut created
4. Test installed application: `todo --help` (from command line)
5. Test uninstaller from Control Panel

---

## Common Development Tasks

### Adding a New Command

1. Create command module in `src/todo_app/infrastructure/cli/commands/`
2. Define Click command with decorators
3. Create corresponding use case in `src/todo_app/application/use_cases/`
4. Register command in `src/todo_app/infrastructure/cli/app.py`
5. Write tests in `tests/unit/infrastructure/` and `tests/integration/`
6. Update `contracts/cli-commands.md` specification

### Adding a New Domain Entity

1. Create entity in `src/todo_app/domain/entities/`
2. Define value objects in `src/todo_app/domain/value_objects/`
3. Add validation rules with Pydantic
4. Write unit tests in `tests/unit/domain/`
5. Update `data-model.md` documentation

### Debugging Tests

```bash
# Run with debugger breakpoint support
pytest --pdb

# Run until first failure
pytest -x

# Show print statements
pytest -s

# Show detailed assertion errors
pytest -vv
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'todo_app'`

**Solution**: Ensure you're in the `phase1-cli` directory and have installed the package:
```bash
cd phase1-cli
uv pip install -e .
```

### Issue: Tests failing with "import errors"

**Solution**: Install dev dependencies:
```bash
uv pip install -e ".[dev]"
```

### Issue: MyPy reports type errors

**Solution**: Check `mypy.ini` configuration and ensure all type hints are present:
```bash
mypy src/todo_app --show-error-codes
```

### Issue: Ruff reports linting violations

**Solution**: Auto-fix most issues:
```bash
ruff check --fix .
ruff format .
```

### Issue: Executable doesn't run on target system

**Solution**: Ensure PyInstaller includes all dependencies:
```bash
# Check for missing modules
pyinstaller --onefile --debug all src/todo_app/__main__.py
# Review warnings in build output
```

### Issue: Rich formatting not displaying correctly

**Solution**: Ensure terminal supports UTF-8:
```powershell
# Windows PowerShell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Or set in registry for persistence
```

---

## Performance Testing

### Measuring Command Execution Time

```bash
# Windows PowerShell
Measure-Command { python -m todo_app add "Test task" }

# Unix (with time command)
time python -m todo_app add "Test task"
```

**Performance Targets**:
- Add task: <100ms
- List 100 tasks: <100ms
- List 1000 tasks: <200ms
- Toggle/Update/Delete: <50ms

### Stress Testing

```bash
# Add 1000 tasks (test script)
python tests/performance/stress_test.py

# Verify no memory leaks
python -m memory_profiler tests/performance/memory_test.py
```

---

## Continuous Integration

### GitHub Actions Workflow

The project includes CI configuration in `.github/workflows/test.yml`:

- Runs tests on push and pull request
- Checks code quality (ruff, mypy)
- Generates coverage report
- Builds executable artifact
- Uploads build to releases

### Local CI Simulation

```bash
# Run full CI pipeline locally
.\scripts\run-ci.ps1

# This executes:
# 1. ruff check
# 2. mypy
# 3. pytest with coverage
# 4. build executable
```

---

## Documentation

### Viewing Documentation

```bash
# Open specifications
code specs/001-cli-todo/spec.md
code specs/001-cli-todo/plan.md
code specs/001-cli-todo/data-model.md
code specs/001-cli-todo/contracts/cli-commands.md
```

### Updating Documentation

When making changes, update relevant documentation:

1. **Spec changes**: Update `specs/001-cli-todo/spec.md`
2. **Architecture changes**: Update `specs/001-cli-todo/plan.md`
3. **Data model changes**: Update `specs/001-cli-todo/data-model.md`
4. **CLI changes**: Update `specs/001-cli-todo/contracts/cli-commands.md`
5. **Create PHR**: Document the change in `history/prompts/`

---

## Release Process

### Creating a Release

1. **Update Version**:
   ```toml
   # pyproject.toml
   version = "1.0.0"
   ```

2. **Update Changelog**:
   ```bash
   code CHANGELOG.md  # Add release notes
   ```

3. **Create Git Tag**:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

4. **Build Artifacts**:
   ```bash
   .\scripts\build.ps1
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" scripts\setup-installer.iss
   ```

5. **Create GitHub Release**:
   - Go to repository releases
   - Create new release from tag v1.0.0
   - Upload `dist/todo-app.exe` and `Output/todo-app-setup.exe`
   - Publish release notes

---

## Next Steps

After completing Phase I:

1. **Test thoroughly**: Run acceptance tests matching spec.md user stories
2. **Performance validation**: Verify all success criteria met
3. **Create PHR**: Document implementation in Prompt History Record
4. **Plan Phase II**: Persistence layer with file/database storage
5. **Gather feedback**: User testing and improvement identification

---

## Support and Resources

- **Project Specification**: `specs/001-cli-todo/spec.md`
- **Architecture Plan**: `specs/001-cli-todo/plan.md`
- **Data Model**: `specs/001-cli-todo/data-model.md`
- **CLI Contracts**: `specs/001-cli-todo/contracts/cli-commands.md`
- **Constitution**: `.specify/memory/constitution.md`
- **Prompt History**: `history/prompts/001-cli-todo/`

---

## Quick Reference

### Essential Commands

| Task | Command |
|------|---------|
| Install dependencies | `uv pip install -e ".[dev]"` |
| Run application | `python -m todo_app [command]` |
| Run tests | `pytest` |
| Run with coverage | `pytest --cov=todo_app --cov-report=html` |
| Lint code | `ruff check .` |
| Format code | `ruff format .` |
| Type check | `mypy src/todo_app` |
| Build executable | `.\scripts\build.ps1` |
| Build installer | `ISCC scripts\setup-installer.iss` |

### Directory Quick Reference

| Path | Purpose |
|------|---------|
| `src/todo_app/domain/` | Business logic, entities |
| `src/todo_app/application/` | Use cases, DTOs |
| `src/todo_app/infrastructure/` | CLI, persistence, formatting |
| `tests/unit/` | Fast isolated tests |
| `tests/integration/` | Cross-layer tests |
| `tests/acceptance/` | User scenario tests |
| `specs/001-cli-todo/` | Feature documentation |

---

**Last Updated**: 2025-12-26  
**Document Version**: 1.0.0  
**Status**: Complete and ready for implementation
