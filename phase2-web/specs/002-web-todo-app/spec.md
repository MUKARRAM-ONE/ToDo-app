# Feature Specification: Phase II Todo Full-Stack Web Application

**Feature Branch**: `002-web-todo-app`  
**Created**: 2026-02-10  
**Status**: Draft  
**Input**: User description: "Transform the Phase I console app into a multi-user web application with persistent storage and authentication."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Secure User Authentication (Priority: P1)

As a new user, I want to sign up with email/password and sign in securely so that my personal todo list is protected and accessible only to me.

**Why this priority**: Foundation for multi-user isolation and data persistence.

**Independent Test**: Register a new user, logout, and log back in to verify access to the personal dashboard.

**Acceptance Scenarios**:

1. **Given** a new visitor, **When** they submit the signup form with valid email and password, **Then** an account is created and they can sign in.
2. **Given** a registered user, **When** they sign in with correct credentials, **Then** they receive a JWT and access to their tasks.
3. **Given** a signed-in user, **When** they sign out, **Then** their session is cleared and they are redirected to signin.

---

### User Story 2 - Task Management Web UI (Priority: P1)

As a user, I want to add, view, update, and delete tasks from a web interface so that I can manage my todos without using a CLI.

**Why this priority**: Core value proposition of the Phase II transition.

**Independent Test**: Create a task via the web form, see it in the list, edit its title, and then delete it.

**Acceptance Scenarios**:

1. **Given** a signed-in user, **When** they add a task with a title, **Then** it appears in their task list.
2. **Given** a task list, **When** a user marks a task as complete, **Then** it is visually updated and persists.
3. **Given** an existing task, **When** a user deletes it, **Then** it is removed from the UI and database.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001: Authentication Flow**: Signup/Signin pages, JWT issuance, secure token storage (httpOnly/localStorage), and protected routes.
- **FR-002: Task CRUD**: Create (title/desc), View (list/card), Update (inline/modal), and Delete (with confirmation).
- **FR-003: User Isolation**: Users MUST only see and manage their own tasks based on authenticated user ID.
- **FR-004: UI Feedback**: Success confirmations for actions and loading states for async operations.

### Key Entities

- **User**: ID (UUID), Email (Unique), Name, Password Hash, Timestamps.
- **Task**: ID (Serial), User ID (FK), Title (Max 200), Description (Text), Completed (Bool), Timestamps.

## API Specification

### Authentication Endpoints
- `POST /api/auth/signup`: Request `{ email, password, name }` -> Response `{ user, session, token }`
- `POST /api/auth/signin`: Request `{ email, password }` -> Response `{ user, session, token }`
- `POST /api/auth/signout`: Request `{ }` -> Response `{ success: true }`

### Task Endpoints
- `GET /api/{user_id}/tasks`: Returns user-specific tasks. Supports query `?status=all|pending|completed`.
- `POST /api/{user_id}/tasks`: Body `{ title, description? }`. Returns created task.
- `GET /api/{user_id}/tasks/{id}`: Returns single task details.
- `PUT /api/{user_id}/tasks/{id}`: Body `{ title?, description? }`. Returns updated task.
- `DELETE /api/{user_id}/tasks/{id}`: Returns `{ success: true }`.
- `PATCH /api/{user_id}/tasks/{id}/complete`: Body `{ completed: boolean }`. Returns updated status.

## Database Schema

### Users Table (managed by Better Auth)
- `id`: string (primary key, UUID)
- `email`: string (unique, not null)
- `name`: string (not null)
- `password_hash`: string (not null)
- `created_at`, `updated_at`: timestamp

### Tasks Table
- `id`: serial (primary key)
- `user_id`: string (foreign key -> users.id, not null)
- `title`: varchar(200) (not null)
- `description`: text (nullable)
- `completed`: boolean (default false)
- `created_at`, `updated_at`: timestamp

**Indexes**: `tasks.user_id`, `tasks.completed`, `users.email`.

## Frontend Pages & Components

### Pages
- `/signup`: Registration
- `/signin`: Login
- `/dashboard`: Main interface (Protected)
- `/`: Landing/Redirect

### Components
- `Layout`: Header, Nav, Footer.
- `TaskList`, `TaskItem`, `TaskForm`.
- `DeleteConfirmation`: Modal for safety.
- `AuthForm`: Reusable logic for auth.

## Success Criteria *(mandatory)*

### Measurable Outcomes
- **SC-001**: API response time < 200ms for CRUD operations.
- **SC-002**: Page load time < 1s for the dashboard.
- **SC-003**: 100% of user data is isolated; no cross-user access possible.
- **SC-004**: Fully responsive UI working on 320px width devices.

## Edge Cases & Error Handling
- **Duplicate Email**: User sees "Email already in use".
- **Expired Token**: User is redirected to signin with a clear message.
- **Empty Title**: Form validation prevents submission.
- **Task Not Found**: 404 response handled gracefully in UI.

## Non-Functional Requirements
- **Security**: Passwords hashed, JWT for all API calls, CORS configured.
- **Accessibility**: WCAG AA compliance (keyboard nav, screen readers).
- **Persistence**: Neon PostgreSQL for serverless reliability.