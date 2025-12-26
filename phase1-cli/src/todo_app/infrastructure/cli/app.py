"""CLI application main entry point."""

import sys
import click
from rich.console import Console

from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
from todo_app.application.use_cases.add_task import AddTaskUseCase
from todo_app.application.use_cases.list_tasks import ListTasksUseCase
from todo_app.application.use_cases.toggle_task import ToggleTaskUseCase
from todo_app.application.use_cases.update_task import UpdateTaskUseCase
from todo_app.application.use_cases.delete_task import DeleteTaskUseCase
from todo_app.infrastructure.cli.formatters.table_formatter import TableFormatter
from todo_app.infrastructure.cli.formatters.message_formatter import MessageFormatter
from todo_app.application.exceptions import TaskNotFoundError

# Initialize shared dependencies
console = Console()
repository = InMemoryTaskRepository()
table_formatter = TableFormatter(console)
message_formatter = MessageFormatter(console)


@click.group()
@click.version_option(version="0.1.0", prog_name="todo")
def cli() -> None:
    """Todo App - Beautiful command-line task manager."""
    pass


@cli.command()
@click.argument("title")
@click.option("--description", "-d", default="", help="Optional task description (0-500 characters)")
def add(title: str, description: str) -> None:
    """Add a new task.
    
    Example:
        todo add "Buy groceries" --description "Milk, eggs, bread"
    """
    try:
        use_case = AddTaskUseCase(repository)
        task_dto = use_case.execute(title=title, description=description)
        
        message_formatter.success(f"Task {task_dto.id} created successfully")
        table_formatter.format_task_details(task_dto)
        
    except Exception as e:
        message_formatter.error(str(e))
        sys.exit(1)


@cli.command()
@click.option("--filter", "-f", "filter_status", default="all", 
              type=click.Choice(["all", "pending", "complete"], case_sensitive=False),
              help="Filter tasks by status")
def list(filter_status: str) -> None:
    """View all tasks.
    
    Example:
        todo list
        todo list --filter pending
        todo list --filter complete
    """
    try:
        use_case = ListTasksUseCase(repository)
        tasks = use_case.execute(filter_status=filter_status.lower())
        
        table_formatter.format_tasks(tasks, filter_status)
        
    except Exception as e:
        message_formatter.error(str(e))
        sys.exit(1)


@cli.command()
@click.argument("task_id")
def toggle(task_id: str) -> None:
    """Mark task as complete/incomplete.
    
    Example:
        todo toggle 1
    """
    try:
        use_case = ToggleTaskUseCase(repository)
        task_dto = use_case.execute(task_id=task_id)
        
        new_status = "complete" if task_dto.status == "complete" else "pending"
        message_formatter.success(f"Task {task_id} marked as {new_status}")
        table_formatter.format_task_details(task_dto)
        
    except TaskNotFoundError as e:
        message_formatter.error(str(e))
        sys.exit(1)
    except Exception as e:
        message_formatter.error(str(e))
        sys.exit(1)


@cli.command()
@click.argument("task_id")
@click.option("--title", "-t", help="New task title")
@click.option("--description", "-d", help="New task description")
def update(task_id: str, title: str, description: str) -> None:
    """Update task details.
    
    Example:
        todo update 1 --title "Buy groceries and fruits"
        todo update 1 --description "Updated description"
        todo update 1 --title "New title" --description "New description"
    """
    try:
        if not title and not description:
            message_formatter.error("At least one option (--title or --description) must be provided")
            sys.exit(1)
        
        use_case = UpdateTaskUseCase(repository)
        task_dto = use_case.execute(
            task_id=task_id,
            title=title if title else None,
            description=description if description else None
        )
        
        message_formatter.success(f"Task {task_id} updated successfully")
        table_formatter.format_task_details(task_dto)
        
    except TaskNotFoundError as e:
        message_formatter.error(str(e))
        sys.exit(1)
    except Exception as e:
        message_formatter.error(str(e))
        sys.exit(1)


@cli.command()
@click.argument("task_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt")
def delete(task_id: str, yes: bool) -> None:
    """Delete a task.
    
    Example:
        todo delete 1
        todo delete 1 --yes
    """
    try:
        # Get task for confirmation
        use_case_list = ListTasksUseCase(repository)
        all_tasks = use_case_list.execute(filter_status="all")
        task_to_delete = next((t for t in all_tasks if t.id == task_id), None)
        
        if not task_to_delete:
            message_formatter.error(f"Task with ID '{task_id}' not found")
            sys.exit(1)
        
        # Confirm deletion
        if not yes:
            confirmed = message_formatter.confirm_delete(task_id, task_to_delete.title)
            if not confirmed:
                message_formatter.info("Deletion cancelled")
                return
        
        # Delete task
        use_case = DeleteTaskUseCase(repository)
        use_case.execute(task_id=task_id)
        
        message_formatter.success(f"Task {task_id} deleted successfully")
        
    except TaskNotFoundError as e:
        message_formatter.error(str(e))
        sys.exit(1)
    except Exception as e:
        message_formatter.error(str(e))
        sys.exit(1)


def main() -> int:
    """Main entry point for the CLI application.

    Returns:
        Exit code (0 for success, non-zero for error)
    """
    try:
        cli()
        return 0
    except Exception as e:
        console.print(f"\n[red]Unexpected error:[/red] {str(e)}\n", style="bold")
        return 2


if __name__ == "__main__":
    sys.exit(main())
