# 🚀 Quick Start Guide - Interactive Todo App

## What You Get

A **user-friendly, interactive console application** where you can:
- ➕ Add tasks continuously
- 📋 View tasks in beautiful tables
- ✓ Mark tasks as complete/incomplete
- ✏️ Update task details
- 🗑️ Delete tasks with confirmation
- 🔍 Search and filter tasks

All without re-running commands! Tasks persist during your session.

---

## 🎯 Three Ways to Run

### 1. **Interactive Mode (Recommended - User Friendly!)**

**Windows:**
```bash
# Double-click this file:
run_todo.bat

# OR run in terminal:
cd phase1-cli
python -m todo_app.interactive
```

**Linux/Mac:**
```bash
chmod +x run_todo.sh
./run_todo.sh

# OR:
python -m todo_app.interactive
```

**What you'll see:**
```
╭────────────────────────────────────────╮
│ Todo App - Interactive Mode            │
│ Manage your tasks easily!              │
╰────────────────────────────────────────╯

Option  Action
1       ➕ Add a new task
2       📋 View all tasks
3       ✓ Mark task as complete/incomplete
4       ✏️ Update a task
5       🗑️ Delete a task
6       🔍 Search/Filter tasks
0       🚪 Exit

Choose an option [0/1/2/3/4/5/6] (2):
```

### 2. **Command-Line Mode (For Advanced Users)**

Run individual commands:

```bash
# Add task
python -m todo_app add "Buy groceries" -d "Milk, eggs, bread"

# List tasks
python -m todo_app list

# Toggle status
python -m todo_app toggle 1

# Update task
python -m todo_app update 1 --title "New title"

# Delete task
python -m todo_app delete 1
```

### 3. **Demo Script (See All Features)**

```bash
python scripts\interactive_demo.py
```

---

## 📖 Interactive Mode Tutorial

### Step 1: Start the App
```bash
python -m todo_app.interactive
```

### Step 2: Add Your First Task
1. Type `1` and press Enter
2. Enter task title: `Buy groceries`
3. Enter description: `Milk, eggs, and bread`
4. Press Enter to return to menu

### Step 3: View Your Tasks
1. Type `2` and press Enter
2. Choose filter: `all` (or `pending`, `complete`)
3. See beautiful table with your tasks!

### Step 4: Mark Task as Complete
1. Type `3` and press Enter
2. Enter task ID: `1`
3. Task is now marked as complete ✓

### Step 5: Update a Task
1. Type `4` and press Enter
2. Enter task ID: `1`
3. Enter new title or description (or press Enter to skip)

### Step 6: Delete a Task
1. Type `5` and press Enter
2. Enter task ID: `1`
3. Confirm deletion

### Step 7: Search Tasks
1. Type `6` and press Enter
2. Enter search term (searches title and description)
3. See filtered results

### Step 8: Exit
Type `0` and press Enter

---

## 💡 Features Showcase

### Beautiful Tables
```
                    📋 All Tasks
┌────┬────────────┬───────────────┬─────────────────┐
│ ID │   Status   │ Title         │ Description     │
├────┼────────────┼───────────────┼─────────────────┤
│ 1  │ ○ Pending  │ Buy groceries │ Milk, eggs...   │
│ 2  │ ✓ Done     │ Call dentist  │ Annual checkup  │
└────┴────────────┴───────────────┴─────────────────┘
```

### Color-Coded Status
- **○ Pending** - Yellow, active tasks
- **✓ Done** - Green, completed tasks (strikethrough)

### Smart Prompts
- Default suggestions for common choices
- Input validation with helpful error messages
- Confirmation prompts for destructive operations

### Search & Filter
- Search by keywords in title or description
- Filter by status: all, pending, or complete
- Quick overview before editing/deleting

---

## ⚙️ Installation

### Prerequisites
- Python 3.13+ installed
- Terminal/Command Prompt

### Setup (One-Time)
```bash
# 1. Navigate to project
cd phase1-cli

# 2. Install dependencies
pip install -e .

# 3. Run the app
python -m todo_app.interactive
```

That's it! 🎉

---

## ⚠️ Important Notes

### Data Persistence
- Tasks are stored **in memory** during your session
- When you exit, tasks are **cleared**
- This is intentional for Phase I
- Phase II will add database persistence

### Console Compatibility
For best experience, use:
- **Windows Terminal** (recommended)
- **VS Code Terminal**
- **PowerShell 7+**
- Any modern terminal with Unicode support

Older CMD.exe may have display issues with emojis.

---

## 🎬 Example Session

```
1. Start app: python -m todo_app.interactive
2. Add task: "Buy groceries" 
3. Add task: "Call dentist"
4. Add task: "Finish homework"
5. View all tasks (shows 3 tasks)
6. Mark task 1 as complete
7. Update task 2 title
8. Delete task 3
9. View pending tasks (shows 1 task)
10. Exit app
```

All in one session, no command re-typing! 🚀

---

## 🆘 Troubleshooting

### App doesn't start
```bash
# Make sure you're in the right directory
cd phase1-cli

# Install dependencies
pip install -e .
pip install rich click pydantic
```

### Unicode characters not displaying
- Use Windows Terminal or modern terminal
- Or run: `python scripts\interactive_demo.py` (no emojis)

### "Module not found" error
```bash
# Install in editable mode
pip install -e .
```

---

## 🎓 Learn More

- **Full Documentation**: See `README.md`
- **Architecture Details**: See `CLAUDE.md`
- **Feature Specification**: See `specs/001-cli-todo/spec.md`
- **Developer Guide**: See `specs/001-cli-todo/plan.md`

---

## 🎯 Next Steps

Ready for more? The application supports:
- Python API for programmatic use
- Command-line mode for scripting
- Extensible architecture for new features

Check out the full `README.md` for advanced usage!

---

**Enjoy managing your tasks! 📝✨**