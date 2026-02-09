"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from todo_app.api.routes import tasks
from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository

_repository = InMemoryTaskRepository()

def get_app() -> FastAPI:
    """Create and configure FastAPI application."""
    app = FastAPI(
        title="Todo API",
        description="Object-Oriented Todo Application with FastAPI",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])
    
    app.state.repository = _repository
    
    @app.get("/")
    async def root() -> dict[str, str]:
        """Root endpoint."""
        return {
            "message": "Welcome to Todo API",
            "docs": "/docs",
            "health": "/health"
        }
    
    @app.get("/health")
    async def health() -> dict[str, str]:
        """Health check endpoint."""
        return {"status": "healthy"}
    
    return app

app = get_app()
