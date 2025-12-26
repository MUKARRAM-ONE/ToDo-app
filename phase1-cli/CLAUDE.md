# Claude Code Instructions

This document provides guidelines for Claude Code when working with the Phase I Todo CLI App.

## Project Overview

**Phase**: I - In-Memory Console Application  
**Architecture**: Clean Architecture (Domain/Application/Infrastructure)  
**Methodology**: Spec-Driven Development + Test-Driven Development  
**Language**: Python 3.13+ with strict type hints

## Core Principles

1. **Spec-First**: All features must have specifications before implementation
2. **Test-Driven**: Write tests first, then implement minimum code to pass
3. **Clean Architecture**: Respect layer boundaries - never skip layers
4. **Type Safety**: 100% type hint coverage, mypy strict mode
5. **Validation**: Pydantic models for all data validation
6. **Documentation**: Self-documenting code with clear docstrings

## Project Structure

```
phase1-cli/
├── src/todo_app/
│   ├── domain/           # Core business logic (no dependencies)
│   ├── application/      # Use cases (depends on domain)
│   └── infrastructure/   # External concerns (depends on application)
├── tests/               # Mirror src structure
├── specs/               # Feature specifications
└── history/             # Prompt History Records
```

## Layer Dependencies

```
Infrastructure → Application → Domain
```

**Rules**:
- Domain layer has ZERO external dependencies
- Application layer depends ONLY on domain
- Infrastructure layer depends on application
- Dependencies flow INWARD only

## Coding Standards

### Type Hints

```python
# ✅ Good
def add_task(title: str, description: str) -> TaskDTO:
    ...

# ❌ Bad
def add_task(title, description):
    ...
```

### Value Objects

```python
# ✅ Good - Always use Pydantic value objects
title = TaskTitle(value="Buy groceries")

# ❌ Bad - Don't use raw strings in domain
title = "Buy groceries"
```

### Error Handling

```python
# ✅ Good - Specific exceptions
raise TaskNotFoundError(f"Task with ID '{task_id}' not found")

# ❌ Bad - Generic exceptions
raise Exception("Task not found")
```

### Repository Pattern

```python
# ✅ Good - Use through interface
class AddTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self._repository = repository

# ❌ Bad - Direct implementation dependency
class AddTaskUseCase:
    def __init__(self, repository: InMemoryTaskRepository):
        self._repository = repository
```

## Testing Guidelines

### Test Structure

```python
# tests/test_[layer]_[component].py
def test_[component]_[scenario]_[expected_behavior]():
    # Arrange
    repository = InMemoryTaskRepository()
    use_case = AddTaskUseCase(repository)
    
    # Act
    result = use_case.execute("Title", "Description")
    
    # Assert
    assert result.title == "Title"
```

### Coverage Requirements

- **Domain Layer**: 100% coverage (no exceptions)
- **Application Layer**: >95% coverage
- **Infrastructure Layer**: >90% coverage
- **Overall**: >90% coverage minimum

### Test Types

1. **Unit Tests**: Test individual components in isolation
2. **Integration Tests**: Test layer interactions
3. **Acceptance Tests**: Test complete user stories

## Common Tasks

### Adding a New Feature

1. **Create specification**: `specs/[feature-name]/spec.md`
2. **Generate plan**: Use `/sp.plan` command
3. **Break into tasks**: Use `/sp.tasks` command
4. **Implement with TDD**:
   - Red: Write failing test
   - Green: Implement minimum code
   - Refactor: Improve quality
5. **Document**: Update README and CHANGELOG
6. **Create PHR**: Document the interaction

### Adding a Use Case

1. Create test: `tests/test_application_[usecase].py`
2. Define interface if needed in `application/interfaces/`
3. Implement use case in `application/use_cases/[usecase].py`
4. Add DTO if needed in `application/dto/`
5. Wire up in CLI: `infrastructure/cli/app.py`

### Adding a Domain Entity

1. Create test: `tests/test_domain_[entity].py`
2. Define value objects in `domain/value_objects/`
3. Create entity in `domain/entities/[entity].py`
4. Add domain exceptions in `domain/exceptions.py`
5. Update DTOs in `application/dto/`

## File Naming Conventions

- **Modules**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: `_leading_underscore`

## Git Workflow

### Branch Naming

- `feature/[feature-name]` - New features
- `bugfix/[bug-name]` - Bug fixes
- `refactor/[component]` - Code refactoring
- `docs/[what]` - Documentation updates

### Commit Messages

Follow Conventional Commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance

Examples:
```
feat(cli): add delete command with confirmation

Implements US5 - Delete task functionality
- Add DeleteTaskUseCase
- Add delete CLI command
- Add confirmation prompt
- Add tests

Closes #5
```

## Quality Checklist

Before considering a task complete:

- [ ] All tests pass (`pytest`)
- [ ] Code coverage >90% (`pytest --cov`)
- [ ] Type checking passes (`mypy src/`)
- [ ] Linting passes (`ruff check .`)
- [ ] Formatting applied (`ruff format .`)
- [ ] Docstrings complete
- [ ] README updated if needed
- [ ] CHANGELOG updated
- [ ] PHR created

## Common Pitfalls

### ❌ Don't Do This

1. **Skip testing**: Never commit untested code
2. **Break layer boundaries**: Don't import infrastructure in domain
3. **Use raw types**: Always use value objects in domain
4. **Ignore validation**: Validate all inputs with Pydantic
5. **Hard-code values**: Use configuration for all settings
6. **Leave TODOs**: Resolve all TODOs before committing
7. **Commit directly**: Always use feature branches

### ✅ Do This Instead

1. **Write tests first**: Red-Green-Refactor cycle
2. **Respect boundaries**: Follow dependency rules
3. **Use value objects**: Encapsulate primitives
4. **Validate early**: Fail fast at layer boundaries
5. **Configure properly**: External concerns in config
6. **Complete work**: No TODOs in committed code
7. **Branch properly**: Feature branches + PR reviews

## Debugging

### Running Tests with Debug Output

```bash
# Verbose output
pytest -v

# Show print statements
pytest -s

# Debug specific test
pytest tests/test_application.py::test_add_task_success -v -s

# Start debugger on failure
pytest --pdb
```

### Type Checking Specific Files

```bash
# Check all
mypy src/

# Check specific module
mypy src/todo_app/domain/

# Show type error context
mypy src/ --show-error-context
```

## AI Interaction Best Practices

When working with Claude Code:

1. **Be specific**: Reference exact files and line numbers
2. **Provide context**: Share relevant code and error messages
3. **Follow TDD**: Request tests before implementation
4. **Ask for review**: Request code review before finalizing
5. **Request documentation**: Ask for docstrings and comments
6. **Validate quality**: Run quality checks after changes

### Example Prompts

**Good Prompts**:
- "Implement AddTaskUseCase following TDD. First create test in tests/test_application.py, then implement in application/use_cases/add_task.py"
- "Refactor TaskRepository interface to support filtering. Update interface and implementation, maintain backward compatibility"
- "Fix mypy error in domain/entities/task.py:45. Error: TaskId type mismatch"

**Avoid**:
- "Add some features" (too vague)
- "Fix the bug" (no context)
- "Make it better" (not specific)

## Resources

### Documentation
- **Constitution**: `.specify/memory/constitution.md`
- **Specification**: `specs/001-cli-todo/spec.md`
- **Plan**: `specs/001-cli-todo/plan.md`
- **Tasks**: `specs/001-cli-todo/tasks.md`

### External Resources
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Click Documentation](https://click.palletsprojects.com/)
- [Rich Documentation](https://rich.readthedocs.io/)
- [pytest Documentation](https://docs.pytest.org/)

## Version Information

**Current Version**: 1.0.0  
**Python Version**: 3.13+  
**Key Dependencies**:
- click >= 8.1.7
- rich >= 13.7.0
- pydantic >= 2.5.0
- pytest >= 7.4.0
- mypy >= 1.7.0
- ruff >= 0.1.0

---

**Remember**: Quality over speed. Take time to do it right the first time.

**When in doubt**: Check the constitution, follow the spec, write the test first.