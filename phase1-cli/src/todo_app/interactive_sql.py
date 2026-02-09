"""Interactive Todo App with SQL database support.

Menu-driven interface for managing tasks stored in PostgreSQL database.
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich import box

from todo_app.infrastructure.persistence.sql_repository import SQLTaskRepository
from todo_app.infrastructure.config.database import get_database_url
from todo_app.application.use_cases.add_task import AddTask
from todo_app.application.use_cases.list_tasks import ListTasks
from todo_app.application.use_cases.toggle_task import ToggleTask
from todo_app.application.use_cases.update_task import UpdateTask
from todo_app.application.use_cases.delete_task import DeleteTask
from todo_app.application.dto.task_filter import TaskFilter
from todo_app.domain.value_objects.task_title import TaskTitle
from todo_app.domain.value_objects.task_description import TaskDescription
from todo_app.domain.enums.task_status import TaskStatus
from todo_app.application.exceptions import TaskNotFoundError
from todo_app.domain.exceptions import ValidationError


console = Console()


def display_menu():
    """Display the main menu."""
    console.print()
    menu = Table(show_header=False, box=box.ROUNDED, border_style="cyan")
    menu.add_column("Option", style="bold yellow", width=3)
    menu.add_column("Action", style="white")
    
    menu.add_row("1", "📝 Add Task")
    menu.add_row("2", "📋 List All Tasks")
    menu.add_row("3", "✅ List Complete Tasks")
    menu.add_row("4", "⏳ List Pending Tasks")
    menu.add_row("5", "✓ Toggle Task Status")
    menu.add_row("6", "✏️  Update Task")
    menu.add_row("7", "🗑️  Delete Task")
    menu.add_row("8", "🚪 Exit")
    
    console.print(Panel(menu, title="[bold cyan]Todo App - Main Menu[/bold cyan]", border_style="cyan"))


def display_tasks(tasks, title="Tasks"):
    """Display tasks in a formatted table."""
    if not tasks:
        console.print(f"\n[yellow]No {title.lower()} found.[/yellow]")
        return
    
    table = Table(show_header=True, box=box.ROUNDED, border_style="green")
    table.add_column("ID", style="cyan", justify="center", width=5)
    table.add_column("Title", style="white", width=30)
    table.add_column("Description", style="dim", width=40)
    table.add_column("Status", justify="center", width=10)
    table.add_column("Created", style="dim", width=19)
    
    for task in tasks:
        status_emoji = "✅" if task.status == TaskStatus.COMPLETE else "⏳"
        status_text = f"{status_emoji} {task.status.value}"
        
        table.add_row(
            str(task.id.value),
            task.title.value,
            task.description.value[:40] if task.description.value else "-",
            status_text,
            task.created_at.strftime("%Y-%m-%d %H:%M:%S")
        )
    
    console.print()
    console.print(Panel(table, title=f"[bold green]{title}[/bold green]", border_style="green"))


def handle_add_task(add_task_use_case):
    """Handle adding a new task."""
    console.print("\n[bold cyan]➕ Add New Task[/bold cyan]")
    
    try:
        title = Prompt.ask("Enter task title")
        description = Prompt.ask("Enter task description (optional)", default="")
        
        result = add_task_use_case.execute(title=title, description=description)
        
        console.print(f"\n[bold green]✓ Task created successfully! (ID: {result.task.id.value})[/bold green]")
        console.print(f"  Title: {result.task.title.value}")
        if result.task.description.value:
            console.print(f"  Description: {result.task.description.value}")
        
    except ValidationError as e:
        console.print(f"\n[bold red]✗ Validation Error: {e}[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]✗ Error: {e}[/bold red]")


def handle_list_tasks(list_tasks_use_case, status_filter=None):
    """Handle listing tasks."""
    task_filter = TaskFilter(status=status_filter) if status_filter else None
    result = list_tasks_use_case.execute(task_filter=task_filter)
    
    if status_filter == TaskStatus.COMPLETE:
        title = "Complete Tasks"
    elif status_filter == TaskStatus.PENDING:
        title = "Pending Tasks"
    else:
        title = "All Tasks"
    
    display_tasks(result.tasks, title)
    console.print(f"\n[dim]Total: {result.count} task(s)[/dim]")


def handle_toggle_task(toggle_task_use_case, list_tasks_use_case):
    """Handle toggling task status."""
    console.print("\n[bold cyan]✓ Toggle Task Status[/bold cyan]")
    
    # Show current tasks first
    result = list_tasks_use_case.execute()
    if not result.tasks:
        console.print("[yellow]No tasks available to toggle.[/yellow]")
        return
    
    display_tasks(result.tasks, "Available Tasks")
    
    try:
        task_id = Prompt.ask("\nEnter task ID to toggle")
        result = toggle_task_use_case.execute(task_id=task_id)
        
        status_text = "complete" if result.task.status == TaskStatus.COMPLETE else "pending"
        console.print(f"\n[bold green]✓ Task #{task_id} marked as {status_text}[/bold green]")
        
    except TaskNotFoundError as e:
        console.print(f"\n[bold red]✗ Error: {e}[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]✗ Error: {e}[/bold red]")


def handle_update_task(update_task_use_case, list_tasks_use_case):
    """Handle updating a task."""
    console.print("\n[bold cyan]✏️  Update Task[/bold cyan]")
    
    # Show current tasks first
    result = list_tasks_use_case.execute()
    if not result.tasks:
        console.print("[yellow]No tasks available to update.[/yellow]")
        return
    
    display_tasks(result.tasks, "Available Tasks")
    
    try:
        task_id = Prompt.ask("\nEnter task ID to update")
        
        console.print("\n[dim]Leave blank to keep current value[/dim]")
        new_title = Prompt.ask("New title", default="")
        new_description = Prompt.ask("New description", default="")
        
        result = update_task_use_case.execute(
            task_id=task_id,
            title=new_title if new_title else None,
            description=new_description if new_description else None
        )
        
        console.print(f"\n[bold green]✓ Task #{task_id} updated successfully[/bold green]")
        console.print(f"  Title: {result.task.title.value}")
        console.print(f"  Description: {result.task.description.value}")
        
    except TaskNotFoundError as e:
        console.print(f"\n[bold red]✗ Error: {e}[/bold red]")
    except ValidationError as e:
        console.print(f"\n[bold red]✗ Validation Error: {e}[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]✗ Error: {e}[/bold red]")


def handle_delete_task(delete_task_use_case, list_tasks_use_case):
    """Handle deleting a task."""
    console.print("\n[bold cyan]🗑️  Delete Task[/bold cyan]")
    
    # Show current tasks first
    result = list_tasks_use_case.execute()
    if not result.tasks:
        console.print("[yellow]No tasks available to delete.[/yellow]")
        return
    
    display_tasks(result.tasks, "Available Tasks")
    
    try:
        task_id = Prompt.ask("\nEnter task ID to delete")
        
        if Confirm.ask(f"Are you sure you want to delete task #{task_id}?"):
            delete_task_use_case.execute(task_id=task_id)
            console.print(f"\n[bold green]✓ Task #{task_id} deleted successfully[/bold green]")
        else:
            console.print("\n[yellow]Delete cancelled[/yellow]")
        
    except TaskNotFoundError as e:
        console.print(f"\n[bold red]✗ Error: {e}[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]✗ Error: {e}[/bold red]")


def main():
    """Main interactive loop."""
    console.print(Panel(
        "[bold cyan]Welcome to Todo App with SQL Database! 🎯[/bold cyan]\n"
        "[dim]Powered by PostgreSQL[/dim]",
        border_style="cyan",
        box=box.DOUBLE
    ))
    
    try:
        # Initialize SQL repository
        db_url = get_database_url()
        repository = SQLTaskRepository(database_url=db_url)
        console.print("[dim]✓ Connected to database successfully[/dim]")
        
        # Initialize use cases
        add_task = AddTask(repository)
        list_tasks = ListTasks(repository)
        toggle_task = ToggleTask(repository)
        update_task = UpdateTask(repository)
        delete_task = DeleteTask(repository)
        
    except ValueError as e:
        console.print(f"\n[bold red]✗ Database Configuration Error:[/bold red]\n{e}")
        return
    except Exception as e:
        console.print(f"\n[bold red]✗ Database Connection Error:[/bold red]\n{e}")
        return
    
    while True:
        display_menu()
        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3", "4", "5", "6", "7", "8"])
        
        if choice == "1":
            handle_add_task(add_task)
        elif choice == "2":
            handle_list_tasks(list_tasks)
        elif choice == "3":
            handle_list_tasks(list_tasks, status_filter=TaskStatus.COMPLETE)
        elif choice == "4":
            handle_list_tasks(list_tasks, status_filter=TaskStatus.PENDING)
        elif choice == "5":
            handle_toggle_task(toggle_task, list_tasks)
        elif choice == "6":
            handle_update_task(update_task, list_tasks)
        elif choice == "7":
            handle_delete_task(delete_task, list_tasks)
        elif choice == "8":
            console.print("\n[bold cyan]👋 Thank you for using Todo App! Goodbye![/bold cyan]\n")
            break


if __name__ == "__main__":
    main()
