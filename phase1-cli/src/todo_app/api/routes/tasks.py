"""Task API routes."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status

from todo_app.application.interfaces.task_repository import TaskRepository
from todo_app.application.use_cases.add_task import AddTaskUseCase
from todo_app.application.use_cases.list_tasks import ListTasksUseCase
from todo_app.application.use_cases.update_task import UpdateTaskUseCase
from todo_app.application.use_cases.toggle_task import ToggleTaskUseCase
from todo_app.application.use_cases.delete_task import DeleteTaskUseCase
from todo_app.application.dto.task_dto import TaskDTO
from todo_app.application.dto.task_filter import TaskFilter
from todo_app.application.exceptions import TaskNotFoundError
from todo_app.domain.enums.task_status import TaskStatus
from todo_app.api.dependencies import get_repository
from todo_app.api.schemas.task_schemas import (
    TaskCreateRequest,
    TaskUpdateRequest,
    TaskResponse,
    TaskListResponse
)

router = APIRouter()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreateRequest,
    repository: TaskRepository = Depends(get_repository)
) -> TaskResponse:
    """Create a new task."""
    use_case = AddTaskUseCase(repository)
    task_dto = use_case.execute(task_data.title, task_data.description)
    return TaskResponse.from_dto(task_dto)

@router.get("/", response_model=TaskListResponse)
async def list_tasks(
    status_filter: Optional[str] = None,
    repository: TaskRepository = Depends(get_repository)
) -> TaskListResponse:
    """List all tasks with optional status filter."""
    filter_str = "all"
    if status_filter:
        if status_filter.lower() not in ["pending", "complete", "all"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid status filter: {status_filter}. Must be one of: all, pending, complete"
            )
        filter_str = status_filter.lower()
    
    use_case = ListTasksUseCase(repository)
    tasks = use_case.execute(filter_str)
    
    return TaskListResponse(
        tasks=[TaskResponse.from_dto(task) for task in tasks],
        total=len(tasks)
    )

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    repository: TaskRepository = Depends(get_repository)
) -> TaskResponse:
    """Get a specific task by ID."""
    task = repository.find_by_id(str(task_id))
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )
    
    task_dto = TaskDTO.from_entity(task)
    return TaskResponse.from_dto(task_dto)

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_data: TaskUpdateRequest,
    repository: TaskRepository = Depends(get_repository)
) -> TaskResponse:
    """Update a task."""
    try:
        use_case = UpdateTaskUseCase(repository)
        task_dto = use_case.execute(str(task_id), task_data.title, task_data.description)
        return TaskResponse.from_dto(task_dto)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )

@router.patch("/{task_id}/toggle", response_model=TaskResponse)
async def toggle_task(
    task_id: int,
    repository: TaskRepository = Depends(get_repository)
) -> TaskResponse:
    """Toggle task status between pending and complete."""
    try:
        use_case = ToggleTaskUseCase(repository)
        task_dto = use_case.execute(str(task_id))
        return TaskResponse.from_dto(task_dto)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    repository: TaskRepository = Depends(get_repository)
) -> None:
    """Delete a task."""
    try:
        use_case = DeleteTaskUseCase(repository)
        use_case.execute(str(task_id))
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )
