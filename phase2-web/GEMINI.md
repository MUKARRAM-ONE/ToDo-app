# Gemini CLI Guidance for Todo-app Phase II

## Monorepo Workflow
This project is structured as a monorepo with:
- `backend/`: FastAPI application
- `frontend/`: Next.js application
- `specs/`: Detailed technical specifications

## Key Principles
- **API-First**: All backend changes must update `specs/api/rest-endpoints.md`.
- **Stateless**: No server-side sessions; use JWT.
- **Type Safety**: Use Pydantic models for Python and TypeScript interfaces for Next.js.

## Development Commands
- Backend: `cd backend && uvicorn app.main:app --reload`
- Frontend: `cd frontend && npm run dev`