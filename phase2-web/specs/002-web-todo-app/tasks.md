# Tasks: Phase II Todo Full-Stack Web Application

**Input**: Design documents from `/specs/002-web-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create monorepo project structure with backend/ and frontend/ directories
- [x] T002 Initialize Next.js 16+ project in frontend/ with TypeScript and Tailwind
- [x] T003 Initialize FastAPI project in backend/ with Python 3.13+ and requirements.txt
- [x] T004 [P] Configure Neon PostgreSQL database and obtain connection string
- [x] T005 [P] Setup environment variables management in backend/.env and frontend/.env.local

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T006 Create SQLModel base models User and Task in backend/app/models.py
- [x] T007 Set up database engine and session management in backend/app/db.py
- [x] T008 Create database initialization script for table creation in backend/app/init_db.py
- [x] T009 [P] Add database indexes for user_id and email in backend/app/models.py
- [x] T010 Implement JWT token generation utility in backend/app/utils/auth.py
- [x] T011 Implement JWT verification middleware/dependency in backend/app/middleware/auth.py
- [x] T012 [P] Implement password hashing utilities in backend/app/utils/auth.py
- [x] T013 Configure CORS middleware in backend/app/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure User Authentication (Priority: P1)

**Goal**: Implement secure signup, signin, and signout with user isolation

**Independent Test**: Register a user, sign in, verify JWT presence, and sign out

- [x] T014 [P] [US1] Define auth schemas (SignUp, SignIn, Token) in backend/app/schemas/auth.py
- [x] T015 [US1] Implement signup route POST /api/auth/signup in backend/app/routes/auth.py
- [x] T016 [US1] Implement signin route POST /api/auth/signin in backend/app/routes/auth.py
- [x] T017 [US1] Implement signout route POST /api/auth/signout in backend/app/routes/auth.py
- [x] T018 [P] [US1] Configure Better Auth in frontend/lib/auth.ts
- [x] T019 [P] [US1] Create Auth context/provider in frontend/context/auth-context.tsx
- [x] T020 [US1] Implement Auth API methods in frontend/lib/api.ts
- [x] T021 [US1] Create reusable AuthForm component in frontend/components/auth/auth-form.tsx
- [x] T022 [P] [US1] Create Signup page in frontend/app/(auth)/signup/page.tsx
- [x] T023 [P] [US1] Create Signin page in frontend/app/(auth)/signin/page.tsx
- [x] T024 [US1] Implement JWT token storage logic in frontend/lib/api.ts
- [x] T025 [P] [US1] Create protected route wrapper component in frontend/components/auth/protected-route.tsx
- [x] T026 [US1] Integrate Auth context with root layout in frontend/app/layout.tsx
- [ ] T027 [US1] Test signup flow manually
- [ ] T028 [US1] Test signin flow manually
- [ ] T029 [US1] Test token persistence across refreshes
- [ ] T030 [US1] Test signout functionality

**Checkpoint**: User Story 1 complete - authentication and user isolation verified

---

## Phase 4: User Story 2 - Basic Task Management (Priority: P1)

**Goal**: Enable users to create and view their personal tasks via web interface

**Independent Test**: Add a task via the web form and verify it appears in the list immediately

- [x] T031 [P] [US2] Define Task schemas in backend/app/schemas/task.py
- [x] T032 [US2] Implement GET /api/{user_id}/tasks endpoint in backend/app/routes/tasks.py
- [x] T033 [US2] Implement POST /api/{user_id}/tasks endpoint in backend/app/routes/tasks.py
- [x] T034 [P] [US2] Add task CRUD methods to frontend/lib/api.ts
- [x] T035 [P] [US2] Create TaskItem component in frontend/components/tasks/task-item.tsx
- [x] T036 [US2] Create TaskList component in frontend/components/tasks/task-list.tsx
- [x] T037 [US2] Create TaskForm (Add mode) in frontend/components/tasks/task-form.tsx
- [x] T038 [P] [US2] Create UI primitives: Button in frontend/components/ui/button.tsx
- [x] T039 [P] [US2] Create UI primitives: Input in frontend/components/ui/input.tsx
- [x] T040 [P] [US2] Create UI primitives: Card in frontend/components/ui/card.tsx
- [x] T041 [US2] Create dashboard layout in frontend/app/(protected)/dashboard/layout.tsx
- [x] T042 [US2] Implement dashboard page in frontend/app/(protected)/dashboard/page.tsx
- [x] T043 [US2] Integrate TaskList and TaskForm in dashboard page
- [x] T044 [US2] Implement loading states for task fetching
- [x] T045 [US2] Implement basic error handling for task operations

**Checkpoint**: User Story 2 complete - users can create and view tasks

---

## Phase 5: User Story 3 - Task Refinement (Priority: P2)

**Goal**: Enable users to edit, delete, and complete tasks

**Independent Test**: Edit an existing task and verify changes persist after refresh

- [x] T046 [US3] Implement PUT /api/{user_id}/tasks/{id} endpoint in backend/app/routes/tasks.py
- [x] T047 [US3] Implement DELETE /api/{user_id}/tasks/{id} endpoint in backend/app/routes/tasks.py
- [x] T048 [US3] Implement PATCH /api/{user_id}/tasks/{id}/complete endpoint in backend/app/routes/tasks.py
- [x] T049 [US3] Update TaskForm to support Edit mode in frontend/components/tasks/task-form.tsx
- [x] T050 [P] [US3] Create DeleteConfirmation modal in frontend/components/tasks/delete-confirmation.tsx
- [x] T051 [US3] Implement "Mark Complete" toggle in frontend/components/tasks/task-item.tsx
- [x] T052 [US3] Implement edit/delete handlers in TaskList component

**Checkpoint**: User Story 3 complete - full task lifecycle managed

---

## Phase 6: Integration & Testing

**Purpose**: Cross-cutting verification and quality assurance

- [x] T053 Verify user isolation in API (users cannot see others' tasks)
- [x] T054 Write backend API tests for Task CRUD using pytest in backend/tests/test_tasks.py
- [x] T055 Write frontend component tests for TaskList in frontend/components/tasks/task-list.test.tsx
- [x] T056 [P] Test responsive design across mobile/desktop
- [x] T057 [P] Perform security audit of JWT handling and CORS
- [x] T058 Perform manual end-to-end regression testing of all features

---

## Phase 7: Deployment & Documentation

**Purpose**: Preparing for release

- [x] T059 [P] Update README.md with full setup and run instructions
- [x] T060 Create deployment guide in docs/deployment.md

---

## DETAILED TASK EXAMPLES

**Task ID:** T006
**Category:** Backend - Database
**Title:** Create SQLModel Database Models
**Description:** Define User and Task SQLModel classes with all fields, relationships, and constraints as specified in the database schema.
**Preconditions:**
- Backend project initialized (T003)
- Neon PostgreSQL database created (T004)
**Specification Reference:** spec.md § Database Schema
**Plan Reference:** plan.md § Backend Component Breakdown
**Files to Create/Modify:**
- backend/app/models.py
**Dependencies:** T003, T004
**Acceptance Criteria:**
- [ ] User model includes: id, email, name, password_hash, created_at, updated_at
- [ ] Task model includes: id, user_id, title, description, completed, created_at, updated_at
- [ ] Foreign key relationship: Task.user_id -> User.id
**Estimated Complexity:** Low

**Task ID:** T032
**Category:** Backend - API
**Title:** Implement GET /api/{user_id}/tasks Endpoint
**Description:** Create FastAPI endpoint to retrieve all tasks for the authenticated user.
**Preconditions:**
- Task model exists (T006)
- Database connection working (T007)
- JWT middleware implemented (T011)
**Specification Reference:** spec.md § API Specification
**Plan Reference:** plan.md § Backend Component Breakdown
**Files to Create/Modify:**
- backend/app/routes/tasks.py
**Dependencies:** T006, T007, T011
**Acceptance Criteria:**
- [ ] Endpoint: GET /api/{user_id}/tasks
- [ ] Returns only tasks belonging to authenticated user
- [ ] Includes all task fields
**Estimated Complexity:** Medium

**Task ID:** T036
**Category:** Frontend - Components
**Title:** Create TaskList Component
**Description:** Build React component that fetches and displays all tasks for the authenticated user.
**Preconditions:**
- API client implemented (T034)
- TaskItem component exists (T035)
**Specification Reference:** spec.md § Frontend Components
**Plan Reference:** plan.md § Frontend Component Breakdown
**Files to Create/Modify:**
- frontend/components/tasks/task-list.tsx
**Dependencies:** T034, T035
**Acceptance Criteria:**
- [ ] Fetches tasks on mount via api.getTasks()
- [ ] Maps tasks to TaskItem components
- [ ] Properly typed with TypeScript
**Estimated Complexity:** Medium

[... Remaining 57 detailed tasks follow same pattern ...]

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Phase 1
- **User Stories (Phase 3+)**: All depend on Phase 2
- **Polish (Final Phases)**: Depend on User Story completion

### Implementation Strategy
1. **MVP First**: Complete Phase 1, 2, 3, and 4 to have a functional Task UI with Auth.
2. **Incremental**: Add Phase 5 for refinement features.
3. **Quality**: Finalize with Phase 6 and 7.
