"""Interactive REPL (Read-Eval-Print Loop) for Todo App.

This provides a user-friendly, menu-driven interface where users can
continuously interact with the todo list without re-running commands.
"""

import sys
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm

from todo_app.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
from todo_app.application.use_cases.add_task import AddTaskUseCase
from todo_app.application.use_cases.list_tasks import ListTasksUseCase
from todo_app.application.use_cases.toggle_task import ToggleTaskUseCase
from todo_app.application.use_cases.update_task import UpdateTaskUseCase
from todo_app.application.use_cases.delete_task import DeleteTaskUseCase
from todo_app.application.exceptions import TaskNotFoundError


class InteractiveTodoApp:
    """Interactive console application for managing tasks."""

    def __init__(self):
        """Initialize the interactive application."""
        self.console = Console()
        self.repository = InMemoryTaskRepository()
        self.running = True

    def clear_screen(self):
        """Clear the console screen."""
        self.console.clear()

    def show_header(self):
        """Display the application header."""
        header = Panel(
            "[bold cyan]Todo App - Interactive Mode[/bold cyan]\n"
            "Manage your tasks easily!",
            style="bold blue",
            border_style="cyan"
        )
        self.console.print(header)
        self.console.print()

    def show_menu(self):
        """Display the main menu."""
        menu = Table(show_header=False, box=None, padding=(0, 2))
        menu.add_column("Option", style="cyan bold", width=8)
        menu.add_column("Action", style="white")
        
        menu.add_row("1", "➕ Add a new task")
        menu.add_row("2", "📋 View all tasks")
        menu.add_row("3", "✓", "Mark task as complete/incomplete")
        menu.add_row("4", "✏️", " Update a task")
        menu.add_row("5", "🗑️", " Delete a task")
        menu.add_row("6", "🔍 Search/Filter tasks")
        menu.add_row("0", "🚪 Exit")
        
        self.console.print(menu)
        self.console.print()

    def get_menu_choice(self) -> str:
        """Get user's menu choice.
        
        Returns:
            User's choice as string
        """
        choice = Prompt.ask(
            "[bold yellow]Choose an option[/bold yellow]",
            choices=["0", "1", "2", "3", "4", "5", "6"],
            default="2"
        )
        return choice

    def add_task_interactive(self):
        """Interactive task addition."""
        self.console.print("\n[bold cyan]➕ Add New Task[/bold cyan]")
        self.console.print("-" * 50)
        
        # Get title
        title = Prompt.ask("[bold]Task title[/bold]")
        if not title.strip():
            self.console.print("[red]✗ Title cannot be empty![/red]")
            input("\nPress Enter to continue...")
            return
        
        # Get description
        description = Prompt.ask(
            "[bold]Description[/bold] (optional, press Enter to skip)",
            default=""
        )
        
        try:
            use_case = AddTaskUseCase(self.repository)
            task_dto = use_case.execute(title=title, description=description)
            
            self.console.print(f"\n[green]✓ Task {task_dto.id} created successfully![/green]")
            self.console.print(f"   Title: {task_dto.title}")
            if task_dto.description:
                self.console.print(f"   Description: {task_dto.description}")
            
        except Exception as e:
            self.console.print(f"\n[red]✗ Error: {str(e)}[/red]")
        
        input("\nPress Enter to continue...")

    def view_tasks_interactive(self):
        """Interactive task viewing."""
        self.console.print("\n[bold cyan]📋 Your Tasks[/bold cyan]")
        self.console.print("-" * 50)
        
        # Ask for filter
        filter_choice = Prompt.ask(
            "[bold]Show tasks[/bold]",
            choices=["all", "pending", "complete"],
            default="all"
        )
        
        try:
            use_case = ListTasksUseCase(self.repository)
            tasks = use_case.execute(filter_status=filter_choice)
            
            if not tasks:
                self.console.print(f"\n[yellow]No {filter_choice} tasks found.[/yellow]")
            else:
                # Create table
                table = Table(
                    title=f"📋 {filter_choice.capitalize()} Tasks",
                    show_header=True,
                    header_style="bold cyan",
                    border_style="blue"
                )
                
                table.add_column("ID", style="dim", width=6)
                table.add_column("Status", width=10, justify="center")
                table.add_column("Title", style="bold")
                table.add_column("Description", style="dim")
                
                for task in tasks:
                    if task.status == "complete":
                        status_icon = "[green]✓ Done[/green]"
                        title_style = "dim strike"
                    else:
                        status_icon = "[yellow]○ Pending[/yellow]"
                        title_style = "white"
                    
                    description = task.description if task.description else "[dim]None[/dim]"
                    if len(description) > 40:
                        description = description[:37] + "..."
                    
                    table.add_row(
                        task.id,
                        status_icon,
                        f"[{title_style}]{task.title}[/{title_style}]",
                        description
                    )
                
                self.console.print("\n")
                self.console.print(table)
                self.console.print(f"\n[dim]Total: {len(tasks)} task(s)[/dim]")
        
        except Exception as e:
            self.console.print(f"\n[red]✗ Error: {str(e)}[/red]")
        
        input("\nPress Enter to continue...")

    def toggle_task_interactive(self):
        """Interactive task status toggle."""
        self.console.print("\n[bold cyan]✓ Toggle Task Status[/bold cyan]")
        self.console.print("-" * 50)
        
        # Show current tasks first
        self._show_quick_task_list()
        
        task_id = Prompt.ask("\n[bold]Enter task ID to toggle[/bold]")
        
        try:
            use_case = ToggleTaskUseCase(self.repository)
            task_dto = use_case.execute(task_id=task_id)
            
            new_status = "complete" if task_dto.status == "complete" else "pending"
            icon = "✓" if new_status == "complete" else "○"
            
            self.console.print(f"\n[green]{icon} Task {task_id} marked as {new_status}![/green]")
            self.console.print(f"   {task_dto.title}")
        
        except TaskNotFoundError:
            self.console.print(f"\n[red]✗ Task with ID '{task_id}' not found![/red]")
        except Exception as e:
            self.console.print(f"\n[red]✗ Error: {str(e)}[/red]")
        
        input("\nPress Enter to continue...")

    def update_task_interactive(self):
        """Interactive task update."""
        self.console.print("\n[bold cyan]✏️  Update Task[/bold cyan]")
        self.console.print("-" * 50)
        
        # Show current tasks first
        self._show_quick_task_list()
        
        task_id = Prompt.ask("\n[bold]Enter task ID to update[/bold]")
        
        # Check if task exists first
        try:
            list_use_case = ListTasksUseCase(self.repository)
            all_tasks = list_use_case.execute("all")
            task = next((t for t in all_tasks if t.id == task_id), None)
            
            if not task:
                self.console.print(f"\n[red]✗ Task with ID '{task_id}' not found![/red]")
                input("\nPress Enter to continue...")
                return
            
            # Show current values
            self.console.print(f"\n[dim]Current title: {task.title}[/dim]")
            self.console.print(f"[dim]Current description: {task.description if task.description else 'None'}[/dim]")
            
            # Get new values
            new_title = Prompt.ask(
                "\n[bold]New title[/bold] (press Enter to keep current)",
                default=""
            )
            
            new_description = Prompt.ask(
                "[bold]New description[/bold] (press Enter to keep current)",
                default=""
            )
            
            if not new_title and not new_description:
                self.console.print("\n[yellow]No changes made.[/yellow]")
                input("\nPress Enter to continue...")
                return
            
            # Update task
            use_case = UpdateTaskUseCase(self.repository)
            task_dto = use_case.execute(
                task_id=task_id,
                title=new_title if new_title else None,
                description=new_description if new_description else None
            )
            
            self.console.print(f"\n[green]✓ Task {task_id} updated successfully![/green]")
            self.console.print(f"   Title: {task_dto.title}")
            if task_dto.description:
                self.console.print(f"   Description: {task_dto.description}")
        
        except Exception as e:
            self.console.print(f"\n[red]✗ Error: {str(e)}[/red]")
        
        input("\nPress Enter to continue...")

    def delete_task_interactive(self):
        """Interactive task deletion."""
        self.console.print("\n[bold cyan]🗑️  Delete Task[/bold cyan]")
        self.console.print("-" * 50)
        
        # Show current tasks first
        self._show_quick_task_list()
        
        task_id = Prompt.ask("\n[bold]Enter task ID to delete[/bold]")
        
        try:
            # Get task details for confirmation
            list_use_case = ListTasksUseCase(self.repository)
            all_tasks = list_use_case.execute("all")
            task = next((t for t in all_tasks if t.id == task_id), None)
            
            if not task:
                self.console.print(f"\n[red]✗ Task with ID '{task_id}' not found![/red]")
                input("\nPress Enter to continue...")
                return
            
            # Confirm deletion
            self.console.print(f"\n[yellow]⚠ You are about to delete:[/yellow]")
            self.console.print(f"   ID: {task.id}")
            self.console.print(f"   Title: {task.title}")
            
            confirmed = Confirm.ask("\n[bold]Are you sure?[/bold]", default=False)
            
            if not confirmed:
                self.console.print("\n[blue]Deletion cancelled.[/blue]")
                input("\nPress Enter to continue...")
                return
            
            # Delete task
            use_case = DeleteTaskUseCase(self.repository)
            use_case.execute(task_id=task_id)
            
            self.console.print(f"\n[green]✓ Task {task_id} deleted successfully![/green]")
        
        except Exception as e:
            self.console.print(f"\n[red]✗ Error: {str(e)}[/red]")
        
        input("\nPress Enter to continue...")

    def search_tasks_interactive(self):
        """Interactive task search/filter."""
        self.console.print("\n[bold cyan]🔍 Search/Filter Tasks[/bold cyan]")
        self.console.print("-" * 50)
        
        search_term = Prompt.ask(
            "[bold]Enter search term[/bold] (searches in title and description)",
            default=""
        )
        
        try:
            use_case = ListTasksUseCase(self.repository)
            all_tasks = use_case.execute("all")
            
            if search_term:
                # Filter tasks by search term
                filtered_tasks = [
                    task for task in all_tasks
                    if search_term.lower() in task.title.lower() or
                       search_term.lower() in (task.description or "").lower()
                ]
            else:
                filtered_tasks = all_tasks
            
            if not filtered_tasks:
                self.console.print(f"\n[yellow]No tasks found matching '{search_term}'[/yellow]")
            else:
                # Display results
                table = Table(
                    title=f"🔍 Search Results ({len(filtered_tasks)} found)",
                    show_header=True,
                    header_style="bold cyan",
                    border_style="blue"
                )
                
                table.add_column("ID", style="dim", width=6)
                table.add_column("Status", width=10)
                table.add_column("Title", style="bold")
                table.add_column("Description", style="dim")
                
                for task in filtered_tasks:
                    status_icon = "[green]✓[/green]" if task.status == "complete" else "[yellow]○[/yellow]"
                    description = task.description if task.description else "[dim]None[/dim]"
                    if len(description) > 40:
                        description = description[:37] + "..."
                    
                    table.add_row(task.id, status_icon, task.title, description)
                
                self.console.print("\n")
                self.console.print(table)
        
        except Exception as e:
            self.console.print(f"\n[red]✗ Error: {str(e)}[/red]")
        
        input("\nPress Enter to continue...")

    def _show_quick_task_list(self):
        """Show a quick overview of tasks."""
        try:
            use_case = ListTasksUseCase(self.repository)
            tasks = use_case.execute("all")
            
            if not tasks:
                self.console.print("[dim]No tasks yet.[/dim]")
                return
            
            self.console.print("\n[dim]Current tasks:[/dim]")
            for task in tasks:
                status = "✓" if task.status == "complete" else "○"
                style = "dim strike" if task.status == "complete" else ""
                self.console.print(f"  [{style}]{status} {task.id}. {task.title}[/{style}]")
        except:
            pass

    def exit_app(self):
        """Exit the application."""
        self.console.print("\n[cyan]👋 Thank you for using Todo App![/cyan]")
        self.console.print("[dim]Your tasks were stored in memory and will be cleared.[/dim]\n")
        self.running = False

    def run(self):
        """Run the interactive application."""
        try:
            while self.running:
                self.clear_screen()
                self.show_header()
                self.show_menu()
                
                choice = self.get_menu_choice()
                
                if choice == "1":
                    self.add_task_interactive()
                elif choice == "2":
                    self.view_tasks_interactive()
                elif choice == "3":
                    self.toggle_task_interactive()
                elif choice == "4":
                    self.update_task_interactive()
                elif choice == "5":
                    self.delete_task_interactive()
                elif choice == "6":
                    self.search_tasks_interactive()
                elif choice == "0":
                    self.exit_app()
        
        except KeyboardInterrupt:
            self.console.print("\n\n[yellow]Operation cancelled by user.[/yellow]")
            self.exit_app()
        except Exception as e:
            self.console.print(f"\n[red]Unexpected error: {str(e)}[/red]")
            sys.exit(1)


def main():
    """Main entry point for interactive mode."""
    app = InteractiveTodoApp()
    app.run()


if __name__ == "__main__":
    main()
