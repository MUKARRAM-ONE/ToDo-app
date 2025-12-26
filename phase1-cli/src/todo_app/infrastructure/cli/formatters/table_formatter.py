"""Table formatter for displaying tasks in a rich table."""

from typing import List
from rich.console import Console
from rich.table import Table

from todo_app.application.dto.task_dto import TaskDTO


class TableFormatter:
    """Formats tasks as a rich table for console display."""

    def __init__(self, console: Console) -> None:
        """Initialize the formatter.
        
        Args:
            console: Rich console instance for output
        """
        self._console = console

    def format_tasks(self, tasks: List[TaskDTO], filter_status: str = "all") -> None:
        """Format and display tasks as a table.
        
        Args:
            tasks: List of tasks to display
            filter_status: Current filter status for header
        """
        # Create table
        table = Table(
            title=f"📋 Todo List ({filter_status.capitalize()})",
            show_header=True,
            header_style="bold cyan",
            border_style="blue",
            title_style="bold magenta"
        )
        
        # Add columns
        table.add_column("ID", style="dim", width=8)
        table.add_column("Status", width=8, justify="center")
        table.add_column("Title", style="bold")
        table.add_column("Description", style="dim")
        
        # Add rows
        if not tasks:
            self._console.print("\n[yellow]No tasks found.[/yellow]\n")
            return
        
        for task in tasks:
            # Status icon and color
            if task.status == "complete":
                status_icon = "[green]✓[/green]"
                title_style = "dim strike"
            else:
                status_icon = "[yellow]○[/yellow]"
                title_style = "white"
            
            # Truncate description if too long
            description = task.description if task.description else ""
            if len(description) > 50:
                description = description[:47] + "..."
            
            # Add row
            table.add_row(
                task.id,
                status_icon,
                f"[{title_style}]{task.title}[/{title_style}]",
                description
            )
        
        # Display table
        self._console.print("\n")
        self._console.print(table)
        self._console.print(f"\n[dim]Total: {len(tasks)} task(s)[/dim]\n")

    def format_task_details(self, task: TaskDTO) -> None:
        """Format and display a single task's details.
        
        Args:
            task: Task to display
        """
        # Status formatting
        if task.status == "complete":
            status_text = "[green]✓ Complete[/green]"
        else:
            status_text = "[yellow]○ Pending[/yellow]"
        
        # Display details
        self._console.print("\n[bold cyan]Task Details:[/bold cyan]")
        self._console.print(f"  ID         : {task.id}")
        self._console.print(f"  Title      : {task.title}")
        self._console.print(f"  Status     : {status_text}")
        self._console.print(f"  Description: {task.description if task.description else '[dim]None[/dim]'}")
        self._console.print(f"  Created    : {task.created_at}\n")
