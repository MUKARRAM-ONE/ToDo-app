"""Interactive Todo CLI session for testing all features.

This script keeps tasks in memory during the session.
Run this to test all features interactively.
"""

from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
from todo_app.application.use_cases.add_task import AddTaskUseCase
from todo_app.application.use_cases.list_tasks import ListTasksUseCase
from todo_app.application.use_cases.toggle_task import ToggleTaskUseCase
from todo_app.application.use_cases.update_task import UpdateTaskUseCase
from todo_app.application.use_cases.delete_task import DeleteTaskUseCase
from todo_app.infrastructure.cli.formatters.table_formatter import TableFormatter
from todo_app.infrastructure.cli.formatters.message_formatter import MessageFormatter
from rich.console import Console


def main():
    """Run interactive demo."""
    console = Console()
    repository = InMemoryTaskRepository()
    table_formatter = TableFormatter(console)
    msg_formatter = MessageFormatter(console)
    
    console.print("\n[bold cyan]Welcome to Todo CLI - Interactive Demo[/bold cyan]\n")
    
    # Demonstrate all features
    console.print("[bold]1. Adding Tasks[/bold]")
    console.print("-" * 60)
    
    # Add tasks
    add_use_case = AddTaskUseCase(repository)
    
    task1 = add_use_case.execute("Buy groceries", "Milk, eggs, bread")
    msg_formatter.success(f"Created task {task1.id}")
    
    task2 = add_use_case.execute("Complete homework", "Math and science assignments")
    msg_formatter.success(f"Created task {task2.id}")
    
    task3 = add_use_case.execute("Call dentist", "Schedule annual checkup")
    msg_formatter.success(f"Created task {task3.id}")
    
    # List all tasks
    console.print("\n[bold]2. Viewing All Tasks[/bold]")
    console.print("-" * 60)
    list_use_case = ListTasksUseCase(repository)
    tasks = list_use_case.execute("all")
    table_formatter.format_tasks(tasks, "all")
    
    # Toggle task
    console.print("[bold]3. Marking Task as Complete[/bold]")
    console.print("-" * 60)
    toggle_use_case = ToggleTaskUseCase(repository)
    updated_task = toggle_use_case.execute("1")
    msg_formatter.success(f"Task {updated_task.id} marked as {updated_task.status}")
    table_formatter.format_task_details(updated_task)
    
    # List pending only
    console.print("[bold]4. Viewing Pending Tasks Only[/bold]")
    console.print("-" * 60)
    pending_tasks = list_use_case.execute("pending")
    table_formatter.format_tasks(pending_tasks, "pending")
    
    # List complete only
    console.print("[bold]5. Viewing Complete Tasks Only[/bold]")
    console.print("-" * 60)
    complete_tasks = list_use_case.execute("complete")
    table_formatter.format_tasks(complete_tasks, "complete")
    
    # Update task
    console.print("[bold]6. Updating Task[/bold]")
    console.print("-" * 60)
    update_use_case = UpdateTaskUseCase(repository)
    updated_task = update_use_case.execute("2", title="Complete homework and review notes")
    msg_formatter.success(f"Task {updated_task.id} updated")
    table_formatter.format_task_details(updated_task)
    
    # View all again
    console.print("[bold]7. Viewing All Tasks After Update[/bold]")
    console.print("-" * 60)
    all_tasks = list_use_case.execute("all")
    table_formatter.format_tasks(all_tasks, "all")
    
    # Delete task
    console.print("[bold]8. Deleting Task[/bold]")
    console.print("-" * 60)
    delete_use_case = DeleteTaskUseCase(repository)
    delete_use_case.execute("3")
    msg_formatter.success("Task 3 deleted")
    
    # Final list
    console.print("[bold]9. Final Task List[/bold]")
    console.print("-" * 60)
    final_tasks = list_use_case.execute("all")
    table_formatter.format_tasks(final_tasks, "all")
    
    console.print("\n[bold green]✓ All features demonstrated successfully![/bold green]\n")
    

if __name__ == "__main__":
    main()
