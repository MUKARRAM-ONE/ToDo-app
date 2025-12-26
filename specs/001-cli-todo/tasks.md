---

description: "Task list for Phase I CLI Todo App implementation following TDD and Clean Architecture"
---

# Tasks: Phase I CLI Todo App

**Input**: Design documents from `/specs/001-cli-todo/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/cli-commands.md, research.md, quickstart.md

**Tests**: Following Test-Driven Development (TDD) approach - tests are written FIRST and MUST FAIL before implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Project root**: `phase1-cli/`
- **Source**: `phase1-cli/src/todo_app/`
- **Tests**: `phase1-cli/tests/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create phase1-cli directory structure with src/todo_app/, tests/, scripts/ folders
- [ ] T002 Initialize pyproject.toml with Python 3.13+, UV configuration, and project metadata
- [ ] T003 [P] Create pytest.ini with test configuration and coverage settings
- [ ] T004 [P] Create mypy.ini with strict type checking configuration
- [ ] T005 [P] Create ruff.toml with linting and formatting rules
- [ ] T006 [P] Create .python-version file specifying Python 3.13
- [ ] T007 Create phase1-cli/src/todo_app/__init__.py package marker
- [ ] T008 Create phase1-cli/src/todo_app/__main__.py entry point
- [ ] T009 [P] Create phase1-cli/tests/__init__.py and tests/conftest.py with shared fixtures
- [ ] T010 Add dependencies to pyproject.toml: click>=8.1.0, rich>=13.0.0, pydantic>=2.5.0
- [ ] T011 [P] Add dev dependencies to pyproject.toml: pytest>=8.0.0, pytest-cov>=4.1.0, mypy>=1.8.0, ruff>=0.1.0
- [ ] T012 Create phase1-cli/README.md with project overview and usage instructions
- [ ] T013 Create phase1-cli/CHANGELOG.md initialized with version 0.1.0

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Domain Layer Foundation

- [ ] T014 [P] Create phase1-cli/src/todo_app/domain/__init__.py
- [ ] T015 [P] Create phase1-cli/src/todo_app/domain/entities/__init__.py
- [ ] T016 [P] Create phase1-cli/src/todo_app/domain/value_objects/__init__.py
- [ ] T017 [P] Create phase1-cli/src/todo_app/domain/enums/__init__.py
- [ ] T018 [P] Create phase1-cli/src/todo_app/domain/exceptions.py with base TodoAppError and DomainError classes

### Domain Value Objects (Red Phase - Write Failing Tests First)

- [ ] T019 [P] Write failing tests in tests/unit/domain/test_task_id.py for TaskId value object validation
- [ ] T020 [P] Write failing tests in tests/unit/domain/test_task_title.py for TaskTitle validation (1-100 chars, non-empty)
- [ ] T021 [P] Write failing tests in tests/unit/domain/test_task_description.py for TaskDescription validation (0-500 chars)
- [ ] T022 [P] Write failing tests in tests/unit/domain/test_task_status.py for TaskStatus enum and display methods

### Domain Value Objects (Green Phase - Implement to Pass Tests)

- [ ] T023 [P] Implement TaskId value object in src/todo_app/domain/value_objects/task_id.py with Pydantic validation
- [ ] T024 [P] Implement TaskTitle value object in src/todo_app/domain/value_objects/task_title.py with length and empty validation
- [ ] T025 [P] Implement TaskDescription value object in src/todo_app/domain/value_objects/task_description.py with length validation
- [ ] T026 [P] Implement TaskStatus enum in src/todo_app/domain/enums/task_status.py with PENDING/COMPLETE and display methods

### Domain Entity (Red-Green)

- [ ] T027 Write failing tests in tests/unit/domain/test_task_entity.py for Task entity business logic
- [ ] T028 Implement Task entity in src/todo_app/domain/entities/task.py with toggle_status, update_title, update_description, is_complete, is_pending methods

### Application Layer Foundation

- [ ] T029 [P] Create phase1-cli/src/todo_app/application/__init__.py
- [ ] T030 [P] Create phase1-cli/src/todo_app/application/interfaces/__init__.py
- [ ] T031 [P] Create phase1-cli/src/todo_app/application/use_cases/__init__.py
- [ ] T032 [P] Create phase1-cli/src/todo_app/application/dto/__init__.py
- [ ] T033 [P] Create phase1-cli/src/todo_app/application/exceptions.py with TaskNotFoundError, ValidationError

### Application DTOs

- [ ] T034 [P] Write failing tests in tests/unit/application/test_task_dto.py for TaskDTO conversion
- [ ] T035 [P] Implement TaskDTO in src/todo_app/application/dto/task_dto.py with from_entity and to_entity methods
- [ ] T036 [P] Write failing tests in tests/unit/application/test_task_filter.py for TaskFilter
- [ ] T037 [P] Implement TaskFilter in src/todo_app/application/dto/task_filter.py with status filtering

### Application Repository Interface

- [ ] T038 Write failing tests in tests/unit/application/test_task_repository_interface.py for repository contract
- [ ] T039 Implement TaskRepository abstract interface in src/todo_app/application/interfaces/task_repository.py with add, get_by_id, get_all, update, delete, count methods

### Infrastructure Layer Foundation

- [ ] T040 [P] Create phase1-cli/src/todo_app/infrastructure/__init__.py
- [ ] T041 [P] Create phase1-cli/src/todo_app/infrastructure/cli/__init__.py
- [ ] T042 [P] Create phase1-cli/src/todo_app/infrastructure/cli/commands/__init__.py
- [ ] T043 [P] Create phase1-cli/src/todo_app/infrastructure/cli/formatters/__init__.py
- [ ] T044 [P] Create phase1-cli/src/todo_app/infrastructure/persistence/__init__.py
- [ ] T045 [P] Create phase1-cli/src/todo_app/infrastructure/config/__init__.py
- [ ] T046 [P] Create phase1-cli/src/todo_app/infrastructure/logging/__init__.py

### Infrastructure - Persistence (Red-Green)

- [ ] T047 Write failing tests in tests/unit/infrastructure/test_in_memory_repository.py for InMemoryTaskRepository CRUD operations
- [ ] T048 Implement InMemoryTaskRepository in src/todo_app/infrastructure/persistence/in_memory_repository.py with dict-based storage

### Infrastructure - Formatters (Red-Green)

- [ ] T049 [P] Write failing tests in tests/unit/infrastructure/test_table_formatter.py for Rich table formatting
- [ ] T050 [P] Write failing tests in tests/unit/infrastructure/test_message_formatter.py for status messages and colors
- [ ] T051 [P] Implement TableFormatter in src/todo_app/infrastructure/cli/formatters/table_formatter.py using Rich Table
- [ ] T052 [P] Implement MessageFormatter in src/todo_app/infrastructure/cli/formatters/message_formatter.py using Rich Console

### Infrastructure - Configuration and Logging

- [ ] T053 [P] Implement Settings in src/todo_app/infrastructure/config/settings.py using Pydantic BaseSettings
- [ ] T054 [P] Implement logger configuration in src/todo_app/infrastructure/logging/logger.py with structured logging

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and Track Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks with title and optional description, receive confirmation with unique ID

**Independent Test**: Launch app, add task with title "Buy groceries", receive confirmation with task ID. This alone delivers value as a quick note-taking tool.

### Tests for User Story 1 (Red Phase - Write Failing Tests FIRST)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T055 [P] [US1] Write failing acceptance test in tests/acceptance/test_user_story_1_add_track.py for complete add task workflow
- [ ] T056 [P] [US1] Write failing integration test in tests/integration/test_add_task_flow.py for CLI command to repository flow
- [ ] T057 [P] [US1] Write failing unit test in tests/unit/application/test_add_task_use_case.py for AddTaskUseCase logic

### Implementation for User Story 1 (Green Phase)

- [ ] T058 [US1] Implement AddTaskUseCase in src/todo_app/application/use_cases/add_task.py with title/description validation and repository integration
- [ ] T059 [US1] Implement add command in src/todo_app/infrastructure/cli/commands/add.py using Click decorators
- [ ] T060 [US1] Wire up add command in src/todo_app/infrastructure/cli/app.py Click application
- [ ] T061 [US1] Implement CLI input validation in src/todo_app/infrastructure/cli/validators.py for add command
- [ ] T062 [US1] Update __main__.py to call CLI app.main() entry point

### Refactor Phase for User Story 1

- [ ] T063 [US1] Run all US1 tests to verify they pass, refactor for clarity without changing behavior
- [ ] T064 [US1] Verify test coverage >90% for AddTaskUseCase and add command

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Enable users to review all tasks in a beautifully formatted table with filtering options

**Independent Test**: Add 2-3 tasks then view the list. Should display a formatted table with all task details. Delivers value as a task inventory tool.

### Tests for User Story 2 (Red Phase - Write Failing Tests FIRST)

- [ ] T065 [P] [US2] Write failing acceptance test in tests/acceptance/test_user_story_2_view_list.py for list display and filtering
- [ ] T066 [P] [US2] Write failing integration test in tests/integration/test_list_tasks_flow.py for CLI to repository flow
- [ ] T067 [P] [US2] Write failing unit test in tests/unit/application/test_list_tasks_use_case.py for ListTasksUseCase with filtering

### Implementation for User Story 2 (Green Phase)

- [ ] T068 [US2] Implement ListTasksUseCase in src/todo_app/application/use_cases/list_tasks.py with status filtering and count summary
- [ ] T069 [US2] Implement list command in src/todo_app/infrastructure/cli/commands/list.py with --status option
- [ ] T070 [US2] Wire up list command in src/todo_app/infrastructure/cli/app.py
- [ ] T071 [US2] Implement empty state handling in MessageFormatter for "no tasks" scenarios

### Refactor Phase for User Story 2

- [ ] T072 [US2] Run all US1 and US2 tests, refactor formatters for reusability
- [ ] T073 [US2] Verify test coverage >90% for ListTasksUseCase and list command

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently (MVP Complete)

---

## Phase 5: User Story 3 - Mark Task Complete (Priority: P2)

**Goal**: Enable users to toggle task status between pending and complete for progress tracking

**Independent Test**: Create a task, mark it complete, view list to see status changed. Delivers value as a progress tracker.

### Tests for User Story 3 (Red Phase - Write Failing Tests FIRST)

- [ ] T074 [P] [US3] Write failing acceptance test in tests/acceptance/test_user_story_3_mark_complete.py for toggle workflow
- [ ] T075 [P] [US3] Write failing integration test in tests/integration/test_toggle_task_flow.py for CLI to repository flow
- [ ] T076 [P] [US3] Write failing unit test in tests/unit/application/test_toggle_task_use_case.py for ToggleTaskUseCase

### Implementation for User Story 3 (Green Phase)

- [ ] T077 [US3] Implement ToggleTaskUseCase in src/todo_app/application/use_cases/toggle_task.py with task existence validation
- [ ] T078 [US3] Implement toggle command in src/todo_app/infrastructure/cli/commands/toggle.py with task_id argument
- [ ] T079 [US3] Wire up toggle command in src/todo_app/infrastructure/cli/app.py
- [ ] T080 [US3] Add status change messages to MessageFormatter for pending/complete transitions

### Refactor Phase for User Story 3

- [ ] T081 [US3] Run all US1-US3 tests, refactor use case error handling
- [ ] T082 [US3] Verify test coverage >90% for ToggleTaskUseCase and toggle command

**Checkpoint**: All high-priority user stories (P1-P2) are now independently functional

---

## Phase 6: User Story 4 - Update Task Details (Priority: P3)

**Goal**: Enable users to modify task title and/or description without losing task ID or status

**Independent Test**: Create a task with typo, update title, verify change in list view.

### Tests for User Story 4 (Red Phase - Write Failing Tests FIRST)

- [ ] T083 [P] [US4] Write failing acceptance test in tests/acceptance/test_user_story_4_update_details.py for update workflow
- [ ] T084 [P] [US4] Write failing integration test in tests/integration/test_update_task_flow.py for CLI to repository flow
- [ ] T085 [P] [US4] Write failing unit test in tests/unit/application/test_update_task_use_case.py for UpdateTaskUseCase

### Implementation for User Story 4 (Green Phase)

- [ ] T086 [US4] Implement UpdateTaskUseCase in src/todo_app/application/use_cases/update_task.py with validation for at least one field
- [ ] T087 [US4] Implement update command in src/todo_app/infrastructure/cli/commands/update.py with --title and --description options
- [ ] T088 [US4] Wire up update command in src/todo_app/infrastructure/cli/app.py
- [ ] T089 [US4] Add validation to ensure at least one field is provided in update command

### Refactor Phase for User Story 4

- [ ] T090 [US4] Run all tests US1-US4, refactor CLI validators for shared validation logic
- [ ] T091 [US4] Verify test coverage >90% for UpdateTaskUseCase and update command

**Checkpoint**: All core CRUD operations are functional

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Enable users to remove obsolete tasks with confirmation to prevent accidental deletion

**Independent Test**: Create a task, delete it with confirmation, verify it no longer appears in list.

### Tests for User Story 5 (Red Phase - Write Failing Tests FIRST)

- [ ] T092 [P] [US5] Write failing acceptance test in tests/acceptance/test_user_story_5_delete_task.py for delete with confirmation
- [ ] T093 [P] [US5] Write failing integration test in tests/integration/test_delete_task_flow.py for CLI to repository flow
- [ ] T094 [P] [US5] Write failing unit test in tests/unit/application/test_delete_task_use_case.py for DeleteTaskUseCase

### Implementation for User Story 5 (Green Phase)

- [ ] T095 [US5] Implement DeleteTaskUseCase in src/todo_app/application/use_cases/delete_task.py with task existence validation
- [ ] T096 [US5] Implement delete command in src/todo_app/infrastructure/cli/commands/delete.py with confirmation prompt and --yes flag
- [ ] T097 [US5] Wire up delete command in src/todo_app/infrastructure/cli/app.py
- [ ] T098 [US5] Implement confirmation prompt using Click.confirm in delete command

### Refactor Phase for User Story 5

- [ ] T099 [US5] Run all tests US1-US5, refactor repository for consistent error handling
- [ ] T100 [US5] Verify test coverage >90% for DeleteTaskUseCase and delete command

**Checkpoint**: All user stories are complete and independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

### Documentation

- [ ] T101 [P] Update README.md with installation instructions, usage examples, and screenshots
- [ ] T102 [P] Create CLAUDE.md with AI assistant context and architectural decisions
- [ ] T103 [P] Update CHANGELOG.md with all implemented features for version 1.0.0
- [ ] T104 [P] Add docstrings to all public APIs in domain, application, and infrastructure layers

### Code Quality and Refactoring

- [ ] T105 Run ruff linting on entire codebase and fix all violations
- [ ] T106 Run mypy type checking in strict mode and resolve all errors
- [ ] T107 [P] Refactor common CLI patterns into reusable utilities
- [ ] T108 [P] Refactor use case error handling for consistency across all use cases
- [ ] T109 Review domain entities for DRY principles and extract common patterns

### Testing Completeness

- [ ] T110 Run full test suite (unit + integration + acceptance) and verify all tests pass
- [ ] T111 Generate coverage report and ensure >90% overall, 100% for domain and application layers
- [ ] T112 [P] Add parametrized tests for edge cases in value object validation
- [ ] T113 [P] Add stress test for 1000 tasks in tests/performance/stress_test.py
- [ ] T114 Validate quickstart.md scenarios by running each command sequence

### Help and User Experience

- [ ] T115 Implement help command in src/todo_app/infrastructure/cli/commands/help.py with command-specific help
- [ ] T116 Add --version flag to main CLI app showing version from pyproject.toml
- [ ] T117 Improve error messages for common user mistakes with actionable guidance
- [ ] T118 Add color-coding to all CLI output for better readability

### Build and Distribution

- [ ] T119 Create build script in scripts/build.ps1 for Windows executable generation with PyInstaller
- [ ] T120 [P] Create build script in scripts/build.sh for Unix/macOS executable generation
- [ ] T121 Test executable generation and verify standalone operation without Python installation
- [ ] T122 Create Inno Setup configuration in scripts/setup-installer.iss for Windows installer
- [ ] T123 Build Windows installer and test installation/uninstallation flow
- [ ] T124 Create run-tests.ps1 script to execute full test suite with coverage

### Version Control and Release

- [ ] T125 Create git tag v1.0.0 for release
- [ ] T126 Create GitHub release notes with feature summary and installation instructions
- [ ] T127 Upload executable artifacts (Windows .exe, installer) to GitHub release

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational completion - MVP Core
- **User Story 2 (Phase 4)**: Depends on Foundational completion - MVP Core
- **User Story 3 (Phase 5)**: Depends on Foundational completion
- **User Story 4 (Phase 6)**: Depends on Foundational completion
- **User Story 5 (Phase 7)**: Depends on Foundational completion
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Integrates with US1 but independently testable (MVP with US1)
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Works with US1/US2 but independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - Works with US1/US2 but independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - Works with US1/US2 but independently testable

### TDD Cycle Dependencies (Within Each User Story)

1. **Red Phase**: Write failing tests first (unit → integration → acceptance)
2. **Green Phase**: Implement minimum code to pass tests
3. **Refactor Phase**: Improve code quality without changing behavior
4. **Tests MUST FAIL before implementation begins**

### Within Each User Story

- Tests (Red Phase) MUST be written and FAIL before implementation (Green Phase)
- Unit tests before integration tests before acceptance tests
- Use cases before CLI commands
- CLI commands before command registration
- Implementation complete and tests passing before refactor phase
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (different files)
- All Foundational tasks marked [P] can run in parallel within their sub-phase
- Once Foundational phase completes, user stories CAN be worked on in parallel by different developers
- Tests for a user story marked [P] can be written in parallel (different test files)
- Value objects and DTOs marked [P] can be implemented in parallel (different files)

---

## Parallel Example: User Story 1 (Add and Track Tasks)

```bash
# RED PHASE - Launch all test files together:
Task T055: "Write failing acceptance test in tests/acceptance/test_user_story_1_add_track.py"
Task T056: "Write failing integration test in tests/integration/test_add_task_flow.py"
Task T057: "Write failing unit test in tests/unit/application/test_add_task_use_case.py"

# Verify all tests FAIL before proceeding to GREEN PHASE

# GREEN PHASE - Implement sequentially (dependencies):
Task T058: "Implement AddTaskUseCase" (depends on domain layer from Phase 2)
Task T059: "Implement add command" (depends on T058)
Task T060: "Wire up add command" (depends on T059)
Task T061: "Implement CLI validation" (can parallel with T060, different file)
Task T062: "Update __main__.py" (depends on T060)

# REFACTOR PHASE - After all tests pass:
Task T063: "Run tests and refactor"
Task T064: "Verify coverage"
```

---

## Parallel Example: Foundational Phase Value Objects

```bash
# RED PHASE - Write all failing tests in parallel:
Task T019: "Write failing tests for TaskId in tests/unit/domain/test_task_id.py"
Task T020: "Write failing tests for TaskTitle in tests/unit/domain/test_task_title.py"
Task T021: "Write failing tests for TaskDescription in tests/unit/domain/test_task_description.py"
Task T022: "Write failing tests for TaskStatus in tests/unit/domain/test_task_status.py"

# Verify all tests FAIL before proceeding to GREEN PHASE

# GREEN PHASE - Implement all value objects in parallel:
Task T023: "Implement TaskId in src/todo_app/domain/value_objects/task_id.py"
Task T024: "Implement TaskTitle in src/todo_app/domain/value_objects/task_title.py"
Task T025: "Implement TaskDescription in src/todo_app/domain/value_objects/task_description.py"
Task T026: "Implement TaskStatus in src/todo_app/domain/enums/task_status.py"

# All value objects are independent - no dependencies between them
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Tasks)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Test US1 and US2 independently
6. Deploy/demo if ready - this is a functional note-taking tool

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Note-taking tool
3. Add User Story 2 → Test independently → Task inventory tool (MVP!)
4. Add User Story 3 → Test independently → Progress tracker
5. Add User Story 4 → Test independently → Full CRUD
6. Add User Story 5 → Test independently → Complete todo app
7. Polish → Production ready
8. Each story adds value without breaking previous stories

### TDD Workflow for Each Story

1. **Red Phase**: Write failing tests (acceptance → integration → unit)
2. **Verify Tests Fail**: Run tests and confirm failures
3. **Green Phase**: Write minimum code to pass tests
4. **Verify Tests Pass**: Run tests and confirm all pass
5. **Refactor Phase**: Improve code quality without breaking tests
6. **Coverage Check**: Verify >90% coverage
7. **Story Complete**: Move to next priority

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Add Tasks)
   - Developer B: User Story 2 (View Tasks)
   - Wait for both US1 and US2 to complete (MVP)
3. After MVP validated:
   - Developer A: User Story 3 (Toggle Status)
   - Developer B: User Story 4 (Update Tasks)
   - Developer C: User Story 5 (Delete Tasks)
4. Team: Polish and distribution together

---

## Summary Statistics

### Total Tasks: 127

### Tasks by Phase:
- Phase 1 (Setup): 13 tasks
- Phase 2 (Foundational): 41 tasks
- Phase 3 (User Story 1 - Add Tasks): 10 tasks
- Phase 4 (User Story 2 - View Tasks): 9 tasks
- Phase 5 (User Story 3 - Toggle Status): 9 tasks
- Phase 6 (User Story 4 - Update Tasks): 9 tasks
- Phase 7 (User Story 5 - Delete Tasks): 9 tasks
- Phase 8 (Polish): 27 tasks

### Tasks by User Story:
- US1 (Add and Track Tasks): 10 tasks
- US2 (View Task List): 9 tasks
- US3 (Mark Task Complete): 9 tasks
- US4 (Update Task Details): 9 tasks
- US5 (Delete Task): 9 tasks

### Parallel Opportunities Identified: 47 tasks marked [P]

### Independent Test Criteria:
- **US1**: Add task with title "Buy groceries", receive confirmation with task ID
- **US2**: Add 2-3 tasks, view formatted table with all details
- **US3**: Create task, mark complete, view list to see status changed
- **US4**: Create task with typo, update title, verify change in list
- **US5**: Create task, delete with confirmation, verify removal from list

### Suggested MVP Scope:
- **Phase 1**: Setup (13 tasks)
- **Phase 2**: Foundational (41 tasks)
- **Phase 3**: User Story 1 (10 tasks)
- **Phase 4**: User Story 2 (9 tasks)
- **Total MVP**: 73 tasks

This provides a fully functional note-taking and task inventory tool ready for user feedback.

---

## Notes

- [P] tasks = different files, no dependencies between them
- [Story] label (US1-US5) maps task to specific user story for traceability
- Each user story should be independently completable and testable
- **TDD CRITICAL**: Verify tests fail before implementing (Red-Green-Refactor)
- Commit after each logical task or story checkpoint
- Stop at any checkpoint to validate story independently
- Run full test suite after each story completion
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Format Validation Checklist

✅ ALL tasks follow checklist format: `- [ ] [ID] [P?] [Story?] Description with file path`
✅ Task IDs are sequential (T001-T127)
✅ [P] markers only on parallelizable tasks (different files, no dependencies)
✅ [Story] labels (US1-US5) only on user story phase tasks
✅ File paths included in all implementation tasks
✅ Tests written BEFORE implementation in TDD approach
✅ Clear phase boundaries with checkpoints
✅ Dependencies documented explicitly
✅ Parallel opportunities identified
✅ MVP scope clearly defined (US1 + US2)
✅ Independent test criteria for each story

**Status**: Ready for immediate execution following TDD and Clean Architecture principles
