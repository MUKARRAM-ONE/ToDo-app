# Quickstart: Phase II Todo App

## Prerequisites
- Node.js 18+
- Python 3.13+
- Neon PostgreSQL Account
- `uv` (Python package manager) or `pip`

## Backend Setup
1. `cd backend`
2. Create virtual env: `uv venv` or `python -m venv .venv`
3. Activate env: `.venv\Scripts\activate` (Windows)
4. Install deps: `uv pip install -r requirements.txt`
5. Configure `.env`:
   ```
   DATABASE_URL=your-neon-url
   JWT_SECRET=your-secret
   CORS_ORIGINS=http://localhost:3000
   ```
6. Run: `uvicorn app.main:app --reload --port 8000`

## Frontend Setup
1. `cd frontend`
2. Install deps: `npm install`
3. Configure `.env.local`:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8000
   BETTER_AUTH_SECRET=your-secret
   BETTER_AUTH_URL=http://localhost:3000
   ```
4. Run: `npm run dev`

## Verification
- Open `http://localhost:3000`
- Navigate to `/signup` to create a new user.
- After signup, you should be redirected to the dashboard.
- Add a task to verify end-to-end connectivity.
