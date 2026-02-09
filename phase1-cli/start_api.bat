@echo off
echo Starting Todo FastAPI Server...
echo.
echo Server will be available at:
echo   - API: http://localhost:8000
echo   - Swagger Docs: http://localhost:8000/docs
echo   - ReDoc: http://localhost:8000/redoc
echo.
echo Press Ctrl+C to stop the server
echo.

cd /d "%~dp0"
python -m todo_app.api.server
