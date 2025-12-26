---
id: PHR-004
title: generate-tasks-cli-todo
stage: tasks
date: 2025-12-26T20:05:32.979Z
surface: CLI
model: Claude 3.5 Sonnet
feature: 001-cli-todo
branch: 001-cli-todo
user: AI Agent
command: /sp.tasks
labels: [tasks, tdd, clean-architecture, phase1-cli]
links:
  spec: specs/001-cli-todo/spec.md
  ticket: null
  adr: specs/001-cli-todo/research.md
  pr: null
files:
  - path: specs/001-cli-todo/tasks.md
    status: created
    lines: 667
tests: []
---

## Prompt

Generate actionable, dependency-ordered tasks for Phase I CLI Todo App implementation.

Requirements:
- Follow Test-Driven Development (TDD) approach
- Start with project setup and configuration
- Implement in order: domain → application → infrastructure → CLI
- Each task should be testable and mergeable
- Include tasks for testing, documentation, and distribution
- Ensure tasks follow clean architecture principles
- Include version tagging and release preparation

Break down by:
1. Project scaffolding (UV, pyproject.toml, directory structure)
2. Domain layer (models, entities, value objects)
3. Application layer (services, use cases)
4. Infrastructure layer (in-memory repository)
5. CLI layer (Click commands, Rich formatting)
6. Testing (unit, integration, coverage)
7. Documentation (README, CLAUDE.md)
8. Build and distribution (PyInstaller, Inno Setup)

## Response snapshot

Generated comprehensive task breakdown (tasks.md) with 127 tasks organized across 8 phases:

**Phase 1: Setup (13 tasks)** - Project initialization, directory structure, configuration files (pyproject.toml, pytest.ini, mypy.ini, ruff.toml)

**Phase 2: Foundational (41 tasks)** - Critical blocking prerequisites following TDD Red-Green-Refactor:
- Domain layer: Value objects (TaskId, TaskTitle, TaskDescription), TaskStatus enum, Task entity
- Application layer: DTOs (TaskDTO, TaskFilter), TaskRepository interface
- Infrastructure: InMemoryTaskRepository, formatters (Table, Message), settings, logging
- All with tests written FIRST (Red phase) before implementation (Green phase)

**Phase 3: User Story 1 - Add and Track Tasks (10 tasks)** - MVP core functionality
- Red phase: Acceptance, integration, unit tests (failing)
- Green phase: AddTaskUseCase, add CLI command, validation
- Refactor phase: Code quality improvements

**Phase 4: User Story 2 - View Task List (9 tasks)** - MVP completion
- Red-Green-Refactor: ListTasksUseCase, list command with filtering
- Completes minimal viable product (add + view tasks)

**Phase 5-7: User Stories 3-5 (27 tasks)** - Additional features (toggle, update, delete)
- Each story follows same TDD pattern
- Independently testable and deliverable

**Phase 8: Polish (27 tasks)** - Documentation, code quality, build, distribution
- Documentation: README, CLAUDE.md, CHANGELOG, docstrings
- Quality: Ruff linting, mypy type checking, refactoring
- Testing: Coverage verification, stress tests, quickstart validation
- Distribution: PyInstaller executable, Inno Setup installer, release artifacts

**Key Features**:
- ✅ All 127 tasks follow strict checklist format: `- [ ] [ID] [P?] [Story?] Description with file path`
- ✅ TDD approach enforced: Tests written FIRST (Red) → Implementation (Green) → Refactor
- ✅ 47 tasks marked [P] for parallel execution
- ✅ Clear phase dependencies with checkpoints
- ✅ MVP scope defined: 73 tasks (Setup + Foundational + US1 + US2)
- ✅ Independent test criteria for each user story
- ✅ Clean Architecture principles maintained throughout

**Task Organization**:
- Setup → Foundational (BLOCKING) → User Stories (parallel-capable) → Polish
- Each user story can be implemented independently after foundational phase
- Clear file paths for all implementation tasks
- Parallel opportunities explicitly marked

## Outcome

- ✅ Impact: Generated 127 actionable, dependency-ordered tasks ready for immediate execution. Tasks follow TDD and Clean Architecture principles with clear phase boundaries.
- 🧪 Tests: TDD approach embedded in task structure - 35 test-related tasks across unit, integration, and acceptance levels. Tests written before implementation in every user story.
- 📁 Files: Created specs/001-cli-todo/tasks.md (667 lines). Tasks cover 53 source files and 25 test files across domain, application, and infrastructure layers.
- 🔁 Next prompts: Execute tasks starting with Phase 1 (Setup), then Phase 2 (Foundational - CRITICAL), then MVP (User Stories 1+2), validate, then continue with remaining user stories and polish.
- 🧠 Reflection: Task breakdown successfully maps user stories from spec.md to concrete implementation steps. TDD cycle (Red-Green-Refactor) is explicit in every user story phase. Parallel opportunities identified (47 tasks) enable efficient team collaboration. MVP scope (73 tasks) provides early validation point.

## Evaluation notes (flywheel)

- Failure modes observed: None - task generation completed successfully with all format requirements met
- Graders run and results (PASS/FAIL): Format validation PASS - all tasks follow checklist format with sequential IDs, appropriate [P] markers, correct [Story] labels, and file paths
- Prompt variant (if applicable): Standard task generation following .specify/templates/tasks-template.md structure
- Next experiment (smallest change to try): Execute Phase 1 and Phase 2 tasks to validate foundational layer before user story implementation
