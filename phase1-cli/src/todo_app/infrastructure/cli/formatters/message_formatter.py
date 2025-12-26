"""Message formatter for displaying success/error messages."""

from rich.console import Console


class MessageFormatter:
    """Formats success, error, and info messages for console display."""

    def __init__(self, console: Console) -> None:
        """Initialize the formatter.
        
        Args:
            console: Rich console instance for output
        """
        self._console = console

    def success(self, message: str) -> None:
        """Display a success message.
        
        Args:
            message: Success message to display
        """
        self._console.print(f"\n[green]✓[/green] {message}\n")

    def error(self, message: str) -> None:
        """Display an error message.
        
        Args:
            message: Error message to display
        """
        self._console.print(f"\n[red]✗ Error:[/red] {message}\n", style="bold")

    def info(self, message: str) -> None:
        """Display an info message.
        
        Args:
            message: Info message to display
        """
        self._console.print(f"\n[blue]ℹ[/blue] {message}\n")

    def warning(self, message: str) -> None:
        """Display a warning message.
        
        Args:
            message: Warning message to display
        """
        self._console.print(f"\n[yellow]⚠[/yellow] {message}\n")

    def confirm_delete(self, task_id: str, task_title: str) -> bool:
        """Display confirmation prompt for task deletion.
        
        Args:
            task_id: ID of task to delete
            task_title: Title of task to delete
            
        Returns:
            True if user confirms, False otherwise
        """
        self._console.print(f"\n[yellow]⚠ Warning:[/yellow] You are about to delete task:")
        self._console.print(f"  ID   : {task_id}")
        self._console.print(f"  Title: {task_title}\n")
        
        response = input("Are you sure? (y/N): ").strip().lower()
        return response in ['y', 'yes']
