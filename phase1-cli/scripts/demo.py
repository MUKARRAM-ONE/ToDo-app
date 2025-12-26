"""Test script demonstrating all Todo CLI features."""

import subprocess
import sys
from pathlib import Path

def run_command(cmd: list[str]) -> tuple[int, str]:
    """Run a CLI command and return result."""
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    return result.returncode, result.stdout + result.stderr

def main():
    """Run comprehensive feature demonstration."""
    print("=" * 60)
    print("Todo CLI - Feature Demonstration")
    print("=" * 60)
    
    # Note: In-memory storage means tasks don't persist between runs
    # This is expected behavior for Phase I
    
    print("\n1. Adding tasks...")
    print("-" * 60)
    code, output = run_command([sys.executable, "-m", "todo_app", "add", "Buy groceries", "-d", "Milk, eggs, bread"])
    print(output)
    
    print("\n2. Viewing help...")
    print("-" * 60)
    code, output = run_command([sys.executable, "-m", "todo_app", "--help"])
    print(output)
    
    print("\n" + "=" * 60)
    print("Demonstration Complete!")
    print("=" * 60)
    print("\nNote: Tasks are stored in-memory and don't persist between runs.")
    print("This is expected behavior for Phase I (Console App).")
    print("\nFor interactive use, consider running commands in a single session")
    print("or wait for Phase II which will include database persistence.")

if __name__ == "__main__":
    main()
