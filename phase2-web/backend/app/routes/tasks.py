from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
from app.db import get_session
from app.models import Task
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.middleware.auth import get_current_user

router = APIRouter()

@router.get("/{user_id}/tasks", response_model=List[TaskResponse])
def get_tasks(
    user_id: str,
    status: Optional[str] = "all",
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access these tasks")
    
    statement = select(Task).where(Task.user_id == user_id)
    if status == "pending":
        statement = statement.where(Task.completed == False)
    elif status == "completed":
        statement = statement.where(Task.completed == True)
        
    tasks = session.exec(statement).all()
    return tasks

@router.post("/{user_id}/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: str,
    task_data: TaskCreate,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not authorized to create tasks for this user")
    
    new_task = Task(
        user_id=user_id,
        title=task_data.title,
        description=task_data.description
    )
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

@router.put("/{user_id}/tasks/{id}", response_model=TaskResponse)
def update_task(
    user_id: str,
    id: int,
    task_data: TaskUpdate,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    task = session.get(Task, id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    
    task.updated_at = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/{user_id}/tasks/{id}")
def delete_task(
    user_id: str,
    id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    task = session.get(Task, id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")
    
    session.delete(task)
    session.commit()
    return {"success": True}

@router.patch("/{user_id}/tasks/{id}/complete", response_model=TaskResponse)
def toggle_task_complete(
    user_id: str,
    id: int,
    complete_data: dict,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    task = session.get(Task, id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.completed = complete_data.get("completed", not task.completed)
    task.updated_at = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task