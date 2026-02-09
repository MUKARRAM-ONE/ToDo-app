from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth, tasks

app = FastAPI(title="Todo App API", version="2.0.0")

# CORS Configuration
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(tasks.router, prefix="/api", tags=["tasks"])

@app.get("/")
async def root():
    return {"message": "Todo App API Phase II is running"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
