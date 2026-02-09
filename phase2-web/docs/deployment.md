# Deployment Guide: Todo App Phase II

## Database (Neon)
1. Use the Neon Console to manage your serverless PostgreSQL instance.
2. Ensure your connection string is secure and stored in environment variables.

## Backend (Railway / Render)
1. Connect your repository to Railway or Render.
2. Set the root directory to `backend`.
3. Configure Environment Variables:
   - `DATABASE_URL`
   - `JWT_SECRET`
   - `ALGORITHM=HS256`
4. Set the start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## Frontend (Vercel)
1. Import your repository into Vercel.
2. Set the root directory to `frontend`.
3. Configure Environment Variables:
   - `NEXT_PUBLIC_API_URL`: Your deployed backend URL.
   - `BETTER_AUTH_SECRET`: A secure random string.
   - `BETTER_AUTH_URL`: Your deployed frontend URL.
4. Deploy!

## Production Checklist
- [ ] Change all default secrets to strong, random values.
- [ ] Disable `echo=True` in `backend/app/db.py`.
- [ ] Ensure CORS origins are restricted to your frontend domain.
- [ ] Enable HTTPS for all endpoints.
