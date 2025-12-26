"""Entry point for running todo_app as a module.

Usage:
    python -m todo_app [command] [options]
"""

import sys

def main() -> int:
    """Main entry point for the todo application."""
    # Import here to avoid circular imports
    from todo_app.infrastructure.cli.app import main as cli_main
    
    return cli_main()


if __name__ == "__main__":
    sys.exit(main())
