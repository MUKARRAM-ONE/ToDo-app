# Todo-app Phase II: Full-Stack Web Application

A modern todo application built with Next.js and FastAPI.

## Project Structure
- `backend/`: FastAPI + SQLModel + PostgreSQL
- `frontend/`: Next.js 16+ + Tailwind CSS + Auth
- `specs/`: Project specifications and tasks

## Setup and Running

### 1. Database (Neon PostgreSQL)
- Create a project on [Neon.tech](https://neon.tech)
- Obtain the `DATABASE_URL`

### 2. Backend Setup
```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
# Unix/macOS
source .venv/bin/activate

pip install -r requirements.txt
```
- Create `.env` from `.env.example` and fill in `DATABASE_URL` and `JWT_SECRET`.
- Run database initialization:
```bash
python -m app.init_db
```
- Start the server:
```bash
uvicorn app.main:app --reload
```

### 3. Frontend Setup
```bash
cd frontend
npm install
```
- Create `.env.local` from `.env.local.example`.
- Start the development server:
```bash
npm run dev
```

## Running Tests
- Backend: `cd backend && pytest`
- Frontend: Requires installing `jest` and `react-testing-library`.

## Key Features
- **Stateless Auth**: JWT-based authentication with user isolation.
- **Responsive UI**: Mobile-first design using Tailwind CSS.
- **Persistent Storage**: Neon PostgreSQL for reliable data management.