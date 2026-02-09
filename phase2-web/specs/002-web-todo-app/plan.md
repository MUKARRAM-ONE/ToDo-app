# Implementation Plan: Phase II Todo Full-Stack Web Application

**Branch**: `002-web-todo-app` | **Date**: 2026-02-10 | **Spec**: [specs/002-web-todo-app/spec.md](spec.md)
**Input**: Feature specification from `/specs/002-web-todo-app/spec.md`

## Summary
Transforming the Phase I console application into a modern, full-stack web application. The solution uses Next.js for a responsive frontend and FastAPI for a high-performance, stateless backend, with Neon PostgreSQL for persistent data storage and Better Auth for secure user management.

## Technical Context

**Language/Version**: Python 3.13+, TypeScript (Next.js 16+)
**Primary Dependencies**: FastAPI, SQLModel, Better Auth, Tailwind CSS
**Storage**: Neon Serverless PostgreSQL
**Testing**: pytest (Backend), Jest/React Testing Library (Frontend)
**Target Platform**: Vercel (Frontend), Railway/Render (Backend)
**Project Type**: Full-stack Web Application
**Performance Goals**: API response < 200ms, Page load < 1s
**Constraints**: Stateless auth (JWT), Independent services, User isolation

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] Independent Services Architecture (Frontend/Backend)
- [x] API-First Design (RESTful JSON)
- [x] Database Persistence (Neon PostgreSQL + SQLModel)
- [x] Stateless Authentication (JWT + Better Auth)
- [x] Responsive & Mobile-First (Tailwind)
- [x] AI-Driven Development (No manual code)

## Project Structure

### Documentation (this feature)

```text
specs/002-web-todo-app/
├── plan.md              # This file
├── research.md          # Technology decisions
├── data-model.md        # Database schema
├── quickstart.md        # Setup guide
├── contracts/           # API definitions
│   ├── auth.md
│   └── tasks.md
└── tasks.md             # Implementation tasks (Phase 2)
```

### Source Code

```text
backend/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── db.py            # DB connection
│   ├── models.py        # SQLModel entities
│   ├── routes/          # API endpoints
│   ├── middleware/      # JWT/Auth
│   └── schemas/         # Pydantic models
└── requirements.txt

frontend/
├── app/                 # Next.js App Router
├── components/          # React components
├── lib/                 # API client & types
└── package.json
```

## System Architecture
The system consists of a Next.js frontend communicating with a FastAPI backend via a RESTful API secured by JWT. Data is stored in Neon PostgreSQL.

## Frontend Component Breakdown
- **Pages**: `signup`, `signin`, `dashboard`.
- **Components**: `TaskList`, `TaskItem`, `TaskForm`, `DeleteConfirmation`.
- **Lib**: `api.ts` (centralized client using `fetch`).

## Backend Component Breakdown
- **Entry**: `main.py` with CORS and Route inclusions.
- **Models**: `User` and `Task` entities via SQLModel.
- **Middleware**: JWT verification using `PyJWT`.
- **Routes**: `auth` for session management, `tasks` for CRUD with user isolation checks.

## Authentication Flow
1. User signs up/in on Frontend via Better Auth.
2. Better Auth/Backend issues JWT.
3. Frontend stores JWT and includes it in `Authorization: Bearer <token>` header for all API calls.
4. Backend middleware verifies token and extracts `user_id`.

## Data Flow
- **Create Task**: Dashboard -> TaskForm -> `api.ts` -> `/api/{user_id}/tasks` -> FastAPI -> SQLModel -> DB.
- **Isolation**: Every backend query filters by `user_id` extracted from the JWT.

## Testing Strategy
- **Backend**: Unit tests for models, Integration tests for API endpoints with a test database.
- **Frontend**: Component testing for UI responsiveness and state management.

## Deployment
- **Frontend**: Automated deployments via Vercel.
- **Backend**: Containerized or git-based deployment on Railway.
- **Database**: Neon Serverless (already running).
