"""SQLTaskRepository - SQL database implementation of TaskRepository."""

from typing import Optional
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from datetime import datetime

from todo_app.application.interfaces.task_repository import TaskRepository
from todo_app.application.dto.task_filter import TaskFilter
from todo_app.application.exceptions import TaskNotFoundError
from todo_app.domain.entities.task import Task
from todo_app.domain.value_objects.task_id import TaskId
from todo_app.domain.value_objects.task_title import TaskTitle
from todo_app.domain.value_objects.task_description import TaskDescription
from todo_app.domain.enums.task_status import TaskStatus

Base = declarative_base()


class TaskModel(Base):
    """SQLAlchemy model for Task entity."""
    
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), default="")
    status = Column(String(20), nullable=False, default="PENDING")
    created_at = Column(DateTime, nullable=False, default=datetime.now)


class SQLTaskRepository(TaskRepository):
    """SQL database implementation of TaskRepository using SQLAlchemy."""
    
    def __init__(self, database_url: Optional[str] = None) -> None:
        """Initialize SQL repository with database connection.
        
        Args:
            database_url: Optional database connection string.
                         If not provided, reads from PSQL_API environment variable.
        """
        if database_url is None:
            database_url = os.getenv('PSQL_API')
            if not database_url:
                raise ValueError("Database URL not provided and PSQL_API environment variable not set")
        
        self.engine = create_engine(database_url, echo=False)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def _to_domain(self, model: TaskModel) -> Task:
        """Convert SQLAlchemy model to domain entity.
        
        Args:
            model: TaskModel instance
            
        Returns:
            Task domain entity
        """
        return Task(
            id=TaskId(value=model.id),
            title=TaskTitle(value=model.title),
            description=TaskDescription(value=model.description or ""),
            status=TaskStatus(model.status),
            created_at=model.created_at
        )
    
    def _to_model(self, task: Task) -> TaskModel:
        """Convert domain entity to SQLAlchemy model.
        
        Args:
            task: Task domain entity
            
        Returns:
            TaskModel instance
        """
        return TaskModel(
            id=task.id.value if task.id.value != 0 else None,
            title=task.title.value,
            description=task.description.value,
            status=task.status.value,
            created_at=task.created_at
        )
    
    def add(self, task: Task) -> Task:
        """Add a new task to the database.
        
        Args:
            task: Task entity to add
            
        Returns:
            Task with assigned ID
        """
        session: Session = self.SessionLocal()
        try:
            model = self._to_model(task)
            model.id = None  # Let database auto-generate
            session.add(model)
            session.commit()
            session.refresh(model)
            return self._to_domain(model)
        finally:
            session.close()
    
    def get_by_id(self, task_id: TaskId) -> Optional[Task]:
        """Retrieve task by ID.
        
        Args:
            task_id: The task identifier
            
        Returns:
            Task entity if found, None otherwise
        """
        session: Session = self.SessionLocal()
        try:
            model = session.query(TaskModel).filter(TaskModel.id == task_id.value).first()
            return self._to_domain(model) if model else None
        finally:
            session.close()
    
    def get_all(self, task_filter: Optional[TaskFilter] = None) -> list[Task]:
        """Retrieve all tasks, optionally filtered.
        
        Args:
            task_filter: Optional filter criteria
            
        Returns:
            List of Task entities matching filter
        """
        session: Session = self.SessionLocal()
        try:
            query = session.query(TaskModel)
            
            if task_filter and task_filter.status is not None:
                query = query.filter(TaskModel.status == task_filter.status.value)
            
            models = query.all()
            return [self._to_domain(model) for model in models]
        finally:
            session.close()
    
    def update(self, task: Task) -> Task:
        """Update existing task.
        
        Args:
            task: Task entity with updated values
            
        Returns:
            Updated task entity
            
        Raises:
            TaskNotFoundError: If task ID doesn't exist
        """
        session: Session = self.SessionLocal()
        try:
            model = session.query(TaskModel).filter(TaskModel.id == task.id.value).first()
            if not model:
                raise TaskNotFoundError(task.id.value)
            
            model.title = task.title.value
            model.description = task.description.value
            model.status = task.status.value
            
            session.commit()
            session.refresh(model)
            return self._to_domain(model)
        finally:
            session.close()
    
    def delete(self, task_id: str) -> None:
        """Delete task by ID (accepts string).
        
        Args:
            task_id: The task identifier as string
            
        Raises:
            TaskNotFoundError: If task ID doesn't exist
        """
        session: Session = self.SessionLocal()
        try:
            int_id = int(task_id)
            model = session.query(TaskModel).filter(TaskModel.id == int_id).first()
            if not model:
                raise TaskNotFoundError(int_id)
            
            session.delete(model)
            session.commit()
        except ValueError:
            raise TaskNotFoundError(task_id)
        finally:
            session.close()
    
    def count(self, task_filter: Optional[TaskFilter] = None) -> int:
        """Count tasks, optionally filtered.
        
        Args:
            task_filter: Optional filter criteria
            
        Returns:
            Number of matching tasks
        """
        return len(self.get_all(task_filter))
    
    def find_by_id(self, task_id: str) -> Optional[Task]:
        """Find task by string ID (convenience method).
        
        Args:
            task_id: Task ID as string
            
        Returns:
            Task entity if found, None otherwise
        """
        try:
            int_id = int(task_id)
            return self.get_by_id(TaskId(value=int_id))
        except (ValueError, AttributeError):
            return None
    
    def find_all(self, task_filter: TaskFilter) -> list[Task]:
        """Find all tasks matching filter (convenience method).
        
        Args:
            task_filter: Filter criteria
            
        Returns:
            List of matching tasks
        """
        return self.get_all(task_filter)
