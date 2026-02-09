"""Server startup script for FastAPI application."""

import uvicorn

def run() -> None:
    """Run the FastAPI server."""
    uvicorn.run(
        "todo_app.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    run()
