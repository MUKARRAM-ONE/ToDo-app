---
id: 001
title: Update constitution for Phase II
stage: constitution
date: 2026-02-10
surface: agent
model: gemini-2.0-flash
feature: none
branch: main
user: J.I TRADERS
command: /sp.constitution
labels: [constitution, phase-ii, full-stack]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - None
---

## Prompt

/sp.constitution Create a comprehensive Constitution file for Phase II of the Todo application.

PHASE II CONTEXT:
- Building: Full-Stack Web Application
- Frontend: Next.js 16+ (App Router), TypeScript, Tailwind CSS
- Backend: FastAPI, SQLModel, Neon PostgreSQL
- Authentication: Better Auth with JWT
- API: RESTful with JWT authentication

CONSTITUTION REQUIREMENTS:

**1. Architecture Principles**
- Clean separation: Frontend (Next.js) and Backend (FastAPI) as independent services
- API-first design: Backend exposes RESTful API, frontend consumes it
- Database-backed: All data persists in Neon PostgreSQL
- Stateless API: JWT for authentication, no session storage
- Responsive design: Mobile-first approach

**2. Technology Constraints**

**Frontend Stack:**
- Next.js 16+ with App Router (not Pages Router)
- TypeScript (strict mode)
- Tailwind CSS (no custom CSS files)
- Better Auth for authentication
- Server Components by default, Client Components only when needed

**Backend Stack:**
- Python 3.13+ with FastAPI
- SQLModel for ORM
- Neon PostgreSQL (serverless)
- JWT for token verification
- Pydantic for request/response validation

**3. Code Standards**

**Frontend:**
- TypeScript strict mode enabled
- All components properly typed
- Server Components by default
- API calls through centralized /lib/api.ts
- Tailwind utility classes only (no inline styles)
- Error boundaries for all pages

**Backend:**
- Type hints for all functions
- Pydantic models for all endpoints
- HTTPException for all errors
- Async/await for all database operations
- Environment variables for all secrets

**4. API Design Principles**
- All endpoints under /api/ prefix
- RESTful conventions (GET, POST, PUT, DELETE, PATCH)
- JWT required in Authorization header
- User-scoped data (users only see their own tasks)
- Consistent error response format
- JSON responses only

**5. Security Requirements**
- JWT tokens for all API requests
- Tokens expire after 7 days
- User ID in URL must match authenticated user
- SQL injection protection via SQLModel
- XSS protection via React
- Environment variables for all secrets
- CORS configured for frontend domain only

**6. Database Principles**
- Use SQLModel models for all tables
- Soft deletes where applicable
- Timestamps (created_at, updated_at) on all tables
- Foreign keys with cascading rules
- Indexes on frequently queried fields
- User isolation via user_id foreign key

**7. User Experience Principles**
- Loading states for all async operations
- Error messages user-friendly
- Success confirmations for all actions
- Responsive design (mobile, tablet, desktop)
- Accessible (WCAG AA compliance)

**8. Testing Requirements**
- API endpoint testing with pytest
- Frontend component testing
- Integration tests for auth flow
- Manual testing of all user journeys

**9. Deployment Constraints**
- Frontend: Vercel (free tier)
- Backend: Separate deployment (Railway, Render, or similar)
- Database: Neon Serverless PostgreSQL
- Environment variables configured properly

**10. Non-Negotiables**
- NO session-based auth (JWT only)
- NO mixed Server/Client components (use proper boundaries)
- NO direct database queries in frontend
- NO hardcoded URLs (use environment variables)
- ALL code generated via AI following specs (no manual coding)

Generate a complete constitution.md file with all sections clearly defined for Phase II full-stack architecture.

## Response snapshot

Created a comprehensive `constitution.md` for Phase II of the Todo application. The new constitution defines architectural principles for a decoupled Next.js/FastAPI stack, technology constraints (Next.js 16+, Python 3.13+, Neon DB), security requirements (JWT), and non-negotiables. Updated the constitution version to 2.0.0.

## Outcome

- ✅ Impact: Established full-stack governance for Phase II.
- 🧪 Tests: None (documentation update).
- 📁 Files: Modified `.specify/memory/constitution.md`.
- 🔁 Next prompts: /sp.specify for the first feature.
- 🧠 Reflection: The detailed prompt provided clear constraints that translated well into the constitution sections.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): PASS.
- Prompt variant (if applicable): N/A.
- Next experiment: N/A.
