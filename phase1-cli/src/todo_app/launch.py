"""Launcher script for Todo App.

This provides an easy way to start the application in different modes.
"""

import sys
import click
from rich.console import Console


@click.command()
@click.option(
    '--mode',
    type=click.Choice(['interactive', 'cli'], case_sensitive=False),
    default='interactive',
    help='Application mode: interactive (menu-driven) or cli (command-based)'
)
def launch(mode: str):
    """Launch Todo App in specified mode.
    
    Interactive mode: Menu-driven interface (default)
    CLI mode: Traditional command-line interface
    """
    console = Console()
    
    if mode.lower() == 'interactive':
        console.print("[bold cyan]Starting Todo App in Interactive Mode...[/bold cyan]\n")
        from todo_app.interactive import main as interactive_main
        interactive_main()
    else:
        console.print("[bold cyan]Todo App - CLI Mode[/bold cyan]")
        console.print("Use: python -m todo_app <command> [options]")
        console.print("Commands: add, list, toggle, update, delete")
        console.print("For help: python -m todo_app --help\n")


if __name__ == "__main__":
    launch()
