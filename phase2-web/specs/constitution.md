<!-- 
<sync_impact_report>
- Version change: 1.0.0 (template) → 2.0.0 (Phase II Full-Stack)
- Modified principles: Entirely redefined for Phase II Web transition.
- Added sections: API Design Principles, Security Requirements, Database Principles, User Experience Principles, Testing Requirements, Deployment Constraints, Non-Negotiables.
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md: Aligned structure for Frontend/Backend separation.
  - ✅ .specify/templates/spec-template.md: Aligned with new functional requirement standards.
  - ✅ .specify/templates/tasks-template.md: Aligned with US-based independent testing.
- Follow-up TODOs: None.
</sync_impact_report>
-->

# Todo-app (Phase II) Constitution

## Core Principles

### I. Independent Services Architecture
The application is split into two independent services: a Next.js frontend and a FastAPI backend. They communicate exclusively via a RESTful API. This separation ensures scalability, maintainability, and clear boundary of concerns.

### II. API-First Design
The backend is the single source of truth and exposes all functionality via a RESTful API. The frontend is a consumer of this API. All API endpoints MUST be prefixed with `/api/` and return JSON responses.

### III. Database Persistence (Neon PostgreSQL)
All data is persisted in Neon Serverless PostgreSQL. The backend uses SQLModel for ORM, ensuring type safety and structured data access. Direct database access from the frontend is strictly forbidden.

### IV. Stateless Authentication (JWT)
The system uses JWT for authentication, ensuring a stateless backend. Better Auth is used on the frontend for auth management. Tokens MUST expire after 7 days, and no session storage is allowed on the backend.

### V. Responsive & Mobile-First Design
The user interface MUST be responsive and accessible (WCAG AA compliant). Tailwind CSS utility classes are the primary styling method, and a mobile-first approach is mandatory for all UI components.

### VI. AI-Driven Development (NON-NEGOTIABLE)
All code MUST be generated via AI following the established specifications and plans. Manual coding should be avoided to ensure consistency and adherence to the architecture.

## Technology Constraints

### Frontend Stack
- Next.js 16+ with App Router (NOT Pages Router).
- TypeScript in strict mode for all components and logic.
- Tailwind CSS for styling (no custom CSS files or inline styles).
- Better Auth for authentication and user management.
- Server Components by default; Client Components used only when interactivity is required.

### Backend Stack
- Python 3.13+ with FastAPI.
- SQLModel for ORM and database modeling.
- Neon Serverless PostgreSQL for data storage.
- JWT for token verification and stateless auth.
- Pydantic for strict request/response validation.

## Code Standards

### Frontend Standards
- All components and functions MUST be properly typed.
- Server/Client boundaries MUST be clearly defined.
- API calls MUST be centralized through `/lib/api.ts`.
- Error boundaries MUST be implemented for all pages.
- Success confirmations and loading states MUST be provided for all async operations.

### Backend Standards
- Type hints are MANDATORY for all functions and models.
- Pydantic models MUST be used for all endpoint inputs and outputs.
- `HTTPException` MUST be used for all error signaling.
- `async/await` MUST be used for all database and I/O operations.
- Environment variables MUST be used for all secrets and configurations.

## API Design Principles
- RESTful conventions (GET, POST, PUT, DELETE, PATCH) are mandatory.
- JWT MUST be included in the `Authorization` header for protected routes.
- User isolation is enforced: users can only see and interact with their own data.
- Consistent error response format is required for all endpoints.

## Security Requirements
- JWT tokens expire after 7 days.
- User ID in URLs MUST match the authenticated user's ID.
- SQL injection protection is enforced via SQLModel.
- XSS protection is provided by React/Next.js default sanitization.
- CORS MUST be configured to allow only the frontend domain.

## Database Principles
- SQLModel models are required for all database tables.
- Soft deletes MUST be implemented where applicable.
- `created_at` and `updated_at` timestamps are required on all tables.
- Foreign keys MUST have cascading rules and proper indexes.
- User isolation via `user_id` foreign key is non-negotiable.

## User Experience Principles
- Loading states for all async operations.
- User-friendly error messages (no raw stack traces).
- Success confirmations for all persistent actions.
- Full responsiveness across mobile, tablet, and desktop.
- WCAG AA compliance for accessibility.

## Testing Requirements
- API endpoints tested using `pytest`.
- Frontend components tested for core functionality.
- Integration tests mandatory for the authentication flow.
- Manual testing of all user journeys before finalization.

## Deployment Constraints
- Frontend: Vercel (Free tier).
- Backend: Railway, Render, or equivalent independent host.
- Database: Neon Serverless PostgreSQL.
- Secrets: Properly configured environment variables in deployment environments.

## Non-Negotiables
- **NO** session-based auth (JWT only).
- **NO** mixed Server/Client components without proper boundaries.
- **NO** direct database queries in the frontend.
- **NO** hardcoded URLs or secrets (use `.env`).
- **ALL** code generated via AI following specs.

## Governance
This constitution supersedes all other development practices in this project. Amendments require a version bump and updated documentation. All plans and tasks must be validated against these principles.

**Version**: 2.0.0 | **Ratified**: 2026-02-10 | **Last Amended**: 2026-02-10