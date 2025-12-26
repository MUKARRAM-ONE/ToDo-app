# CLI Commands Contract Specification

**Feature**: 001-cli-todo  
**Date**: 2025-12-26  
**Status**: Complete

## Overview

This document defines the complete command-line interface contract for the Phase I Todo application. All commands follow Click framework conventions with consistent error handling and output formatting.

---

## Global Options

All commands support these global options:

```yaml
global_options:
  --help:
    short: -h
    description: Show help message and exit
    type: flag
  
  --version:
    short: -v
    description: Show application version
    type: flag
```

---

## Command: `todo add`

**Description**: Add a new task to the todo list.

**Usage**:
```bash
todo add "Task title" [OPTIONS]
```

**Arguments**:

```yaml
arguments:
  title:
    description: The task title (1-100 characters)
    type: string
    required: true
    position: 1
    constraints:
      - min_length: 1
      - max_length: 100
      - not_empty: true
```

**Options**:

```yaml
options:
  --description:
    short: -d
    description: Optional task description (0-500 characters)
    type: string
    required: false
    default: ""
    constraints:
      - max_length: 500
```

**Examples**:

```bash
# Basic task with title only
todo add "Buy groceries"

# Task with description
todo add "Call dentist" --description "Schedule annual checkup"
todo add "Call dentist" -d "Schedule annual checkup"

# Task with multi-word title (quotes required)
todo add "Complete project documentation"
```

**Success Output**:

```
✓ Task 1 created successfully

  ID    : 1
  Title : Buy groceries
  Status: ○ Pending
```

**Error Cases**:

| Error | Condition | Output | Exit Code |
|-------|-----------|--------|-----------|
| Empty title | Title is empty or whitespace | `Error: Title cannot be empty` | 1 |
| Title too long | Title exceeds 100 chars | `Error: Title cannot exceed 100 characters` | 1 |
| Description too long | Description exceeds 500 chars | `Error: Description cannot exceed 500 characters` | 1 |

---

## Command: `todo list`

**Description**: Display all tasks in a formatted table.

**Usage**:
```bash
todo list [OPTIONS]
```

**Arguments**: None

**Options**:

```yaml
options:
  --status:
    short: -s
    description: Filter by status (all, pending, complete)
    type: choice
    choices: [all, pending, complete]
    required: false
    default: all
```

**Examples**:

```bash
# List all tasks
todo list

# List only pending tasks
todo list --status pending
todo list -s pending

# List only completed tasks
todo list --status complete
todo list -s complete
```

**Success Output** (with tasks):

```
┌────┬────────┬──────────────────────┬─────────────────────────────┐
│ ID │ Status │ Title                │ Description                 │
├────┼────────┼──────────────────────┼─────────────────────────────┤
│ 1  │ ○      │ Buy groceries        │ Milk, eggs, bread           │
│ 2  │ ✓      │ Call dentist         │ Schedule annual checkup     │
│ 3  │ ○      │ Finish project docs  │                             │
└────┴────────┴──────────────────────┴─────────────────────────────┘

Total: 3 tasks (2 pending, 1 complete)
```

**Success Output** (no tasks):

```
No tasks yet. Use 'todo add' to create your first task!
```

**Success Output** (filtered, no matches):

```
No complete tasks found.
```

**Error Cases**:

| Error | Condition | Output | Exit Code |
|-------|-----------|--------|-----------|
| Invalid status | Status not in [all, pending, complete] | `Error: Invalid status. Choose from: all, pending, complete` | 1 |

---

## Command: `todo toggle`

**Description**: Toggle task status between pending and complete.

**Usage**:
```bash
todo toggle TASK_ID
```

**Arguments**:

```yaml
arguments:
  task_id:
    description: The ID of the task to toggle
    type: integer
    required: true
    position: 1
    constraints:
      - min_value: 1
```

**Options**: None

**Examples**:

```bash
# Toggle task 1 from pending to complete
todo toggle 1

# Toggle task 2 from complete to pending
todo toggle 2
```

**Success Output** (pending → complete):

```
✓ Task 1 marked as complete
```

**Success Output** (complete → pending):

```
○ Task 1 marked as pending
```

**Error Cases**:

| Error | Condition | Output | Exit Code |
|-------|-----------|--------|-----------|
| Task not found | Task ID doesn't exist | `Error: Task ID 999 not found` | 1 |
| Invalid ID | ID is not a positive integer | `Error: Task ID must be a positive integer` | 1 |

---

## Command: `todo update`

**Description**: Update task title and/or description.

**Usage**:
```bash
todo update TASK_ID [OPTIONS]
```

**Arguments**:

```yaml
arguments:
  task_id:
    description: The ID of the task to update
    type: integer
    required: true
    position: 1
    constraints:
      - min_value: 1
```

**Options**:

```yaml
options:
  --title:
    short: -t
    description: New task title (1-100 characters)
    type: string
    required: false
    constraints:
      - min_length: 1
      - max_length: 100
  
  --description:
    short: -d
    description: New task description (0-500 characters)
    type: string
    required: false
    constraints:
      - max_length: 500
```

**Validation**: At least one of `--title` or `--description` must be provided.

**Examples**:

```bash
# Update title only
todo update 1 --title "Buy groceries and pharmacy items"
todo update 1 -t "Buy groceries and pharmacy items"

# Update description only
todo update 2 --description "Call tomorrow at 9 AM"
todo update 2 -d "Call tomorrow at 9 AM"

# Update both title and description
todo update 3 --title "Complete project" --description "Focus on documentation"
todo update 3 -t "Complete project" -d "Focus on documentation"
```

**Success Output**:

```
✓ Task 1 updated successfully

  ID         : 1
  Title      : Buy groceries and pharmacy items
  Description: Milk, eggs, bread
  Status     : ○ Pending
```

**Error Cases**:

| Error | Condition | Output | Exit Code |
|-------|-----------|--------|-----------|
| Task not found | Task ID doesn't exist | `Error: Task ID 999 not found` | 1 |
| No fields provided | Neither --title nor --description given | `Error: At least one of --title or --description must be provided` | 1 |
| Empty title | New title is empty or whitespace | `Error: Title cannot be empty` | 1 |
| Title too long | New title exceeds 100 chars | `Error: Title cannot exceed 100 characters` | 1 |
| Description too long | New description exceeds 500 chars | `Error: Description cannot exceed 500 characters` | 1 |

---

## Command: `todo delete`

**Description**: Delete a task permanently with confirmation.

**Usage**:
```bash
todo delete TASK_ID [OPTIONS]
```

**Arguments**:

```yaml
arguments:
  task_id:
    description: The ID of the task to delete
    type: integer
    required: true
    position: 1
    constraints:
      - min_value: 1
```

**Options**:

```yaml
options:
  --yes:
    short: -y
    description: Skip confirmation prompt
    type: flag
    required: false
    default: false
```

**Examples**:

```bash
# Delete with confirmation prompt
todo delete 1

# Delete without confirmation (force)
todo delete 1 --yes
todo delete 1 -y
```

**Interactive Flow** (without `--yes`):

```
Delete task 1 "Buy groceries"? [y/N]: y
✓ Task 1 deleted successfully
```

```
Delete task 1 "Buy groceries"? [y/N]: n
Deletion cancelled
```

**Success Output** (with `--yes`):

```
✓ Task 1 deleted successfully
```

**Error Cases**:

| Error | Condition | Output | Exit Code |
|-------|-----------|--------|-----------|
| Task not found | Task ID doesn't exist | `Error: Task ID 999 not found` | 1 |
| Invalid ID | ID is not a positive integer | `Error: Task ID must be a positive integer` | 1 |

---

## Command: `todo help`

**Description**: Display help information for all commands.

**Usage**:
```bash
todo help [COMMAND]
```

**Arguments**:

```yaml
arguments:
  command:
    description: Specific command to get help for
    type: choice
    choices: [add, list, toggle, update, delete]
    required: false
    position: 1
```

**Examples**:

```bash
# General help
todo help

# Help for specific command
todo help add
todo help list
```

**Success Output** (general):

```
Todo App - Command Line Task Manager

Usage: todo [COMMAND] [OPTIONS]

Commands:
  add      Add a new task
  list     Display all tasks
  toggle   Toggle task status
  update   Update task details
  delete   Delete a task
  help     Show help information

Use 'todo help COMMAND' for detailed information on a specific command.
```

**Success Output** (specific command):

```
todo add - Add a new task

Usage: todo add TITLE [OPTIONS]

Arguments:
  TITLE    The task title (1-100 characters)

Options:
  -d, --description TEXT  Optional task description (0-500 characters)
  -h, --help              Show this help message

Examples:
  todo add "Buy groceries"
  todo add "Call dentist" -d "Schedule annual checkup"
```

---

## Exit Codes

| Code | Meaning | When Used |
|------|---------|-----------|
| 0 | Success | Command completed without errors |
| 1 | User Error | Invalid input, validation failure, task not found |
| 2 | System Error | Unexpected exception, internal error |

---

## Output Formatting Standards

### Success Messages

```yaml
format: "[symbol] [message]"
symbols:
  success: "✓" (green checkmark)
  pending: "○" (yellow circle)
  complete: "✓" (green checkmark)
colors:
  success: green
  error: red
  warning: yellow
  info: cyan
```

### Error Messages

```yaml
format: "Error: [message]"
color: red
style: bold
```

### Table Formatting

```yaml
table:
  borders: rounded (┌─┐│└─┘)
  header_style: bold cyan
  columns:
    id: right-aligned, cyan
    status: center-aligned, colored by status
    title: left-aligned, white
    description: left-aligned, dim white
  max_width: terminal width - 4
  description_truncate: "..." if exceeds column width
```

---

## Internationalization (Future)

**Phase I**: English only
**Future Phases**: Localization support with message keys

---

## Accessibility Considerations

1. **Color Independence**: Status symbols (○, ✓) work without color
2. **Screen Reader Friendly**: Plain text output before Rich formatting
3. **Keyboard Only**: No mouse interaction required
4. **Clear Error Messages**: Actionable guidance for all errors

---

## Integration with Use Cases

| Command | Use Case | Application Layer |
|---------|----------|-------------------|
| `todo add` | AddTaskUseCase | `application/use_cases/add_task.py` |
| `todo list` | ListTasksUseCase | `application/use_cases/list_tasks.py` |
| `todo toggle` | ToggleTaskUseCase | `application/use_cases/toggle_task.py` |
| `todo update` | UpdateTaskUseCase | `application/use_cases/update_task.py` |
| `todo delete` | DeleteTaskUseCase | `application/use_cases/delete_task.py` |

---

## Testing Requirements

### Command Testing

Each command must have:

1. **Unit Tests** (CLI layer)
   - Argument parsing validation
   - Option handling
   - Error message formatting

2. **Integration Tests** (CLI + Use Case)
   - Successful command execution
   - Error case handling
   - Output formatting verification

3. **Acceptance Tests** (E2E)
   - User scenario workflows
   - Multi-command sequences
   - Real terminal interaction simulation

### Test Coverage Targets

- 100% of command handlers
- 100% of error paths
- 100% of validation rules
- All examples from this specification

---

## Implementation Checklist

- ✅ All commands specified with arguments and options
- ✅ Success and error outputs defined
- ✅ Examples provided for each command
- ✅ Exit codes standardized
- ✅ Output formatting conventions established
- ✅ Use case integration mapped
- ✅ Testing requirements defined
- ✅ Accessibility considerations documented

**Status**: Ready for implementation (Phase 2 task breakdown)
