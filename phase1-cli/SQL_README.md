# Todo App with SQL Database Support

A fully functional console-based Todo application with PostgreSQL database integration.

## Features

- ✅ Add, update, delete, and list tasks
- ✅ Mark tasks as complete/pending
- ✅ Persistent storage with PostgreSQL (Neon.tech)
- ✅ Beautiful interactive menu interface
- ✅ Clean architecture with Domain-Driven Design

## Prerequisites

- Python 3.13+
- PostgreSQL database (Neon.tech or local)

## Installation

1. Navigate to the project directory:
```bash
cd phase1-cli
```

2. Install dependencies:
```bash
pip install sqlalchemy psycopg2-binary python-dotenv
```

Or install the package:
```bash
pip install -e .
```

## Configuration

1. Create or update `.env` file in the `phase1-cli` directory:
```env
PSQL_API=postgresql://user:password@host:port/database
```

Your current configuration is already set in `.env`:
```env
PSQL_API=postgresql://neondb_owner:npg_Z9fFLM1bHwvh@ep-twilight-resonance-a83r107a-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require
```

## Usage

### Run with SQL Database

Start the interactive console app with SQL database:

```bash
python -m todo_app.interactive_sql
```

### Run with In-Memory Storage (Original)

If you want to use the original in-memory version:

```bash
python -m todo_app.interactive
```

## Menu Options

1. **📝 Add Task** - Create a new task with title and description
2. **📋 List All Tasks** - View all tasks
3. **✅ List Complete Tasks** - View only completed tasks
4. **⏳ List Pending Tasks** - View only pending tasks
5. **✓ Toggle Task Status** - Mark task as complete/pending
6. **✏️ Update Task** - Modify task title or description
7. **🗑️ Delete Task** - Remove a task
8. **🚪 Exit** - Close the application

## Database Schema

The application automatically creates a `tasks` table with the following structure:

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(500) DEFAULT '',
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

## Architecture

The application follows Clean Architecture principles:

```
domain/          - Business entities and rules
├── entities/    - Task entity
├── value_objects/ - TaskId, TaskTitle, TaskDescription
└── enums/       - TaskStatus

application/     - Use cases and business logic
├── use_cases/   - AddTask, ListTasks, ToggleTask, etc.
└── interfaces/  - TaskRepository (abstract)

infrastructure/  - External integrations
├── persistence/ - InMemoryRepository, SQLTaskRepository
└── config/      - Database configuration
```

## Repository Implementations

### SQLTaskRepository
- Uses SQLAlchemy ORM
- Connects to PostgreSQL via connection string
- Automatic table creation
- Full CRUD operations

### InMemoryTaskRepository (Original)
- Dictionary-based storage
- No persistence
- Fast for testing

## Example Usage

```python
# The app will guide you through the menu
$ python -m todo_app.interactive_sql

Welcome to Todo App with SQL Database! 🎯
Powered by PostgreSQL
✓ Connected to database successfully

╭─────────────── Todo App - Main Menu ───────────────╮
│ 1   📝 Add Task                                     │
│ 2   📋 List All Tasks                               │
│ 3   ✅ List Complete Tasks                          │
│ 4   ⏳ List Pending Tasks                           │
│ 5   ✓ Toggle Task Status                           │
│ 6   ✏️  Update Task                                 │
│ 7   🗑️  Delete Task                                 │
│ 8   🚪 Exit                                         │
╰─────────────────────────────────────────────────────╯

Enter your choice [1/2/3/4/5/6/7/8]: 1

➕ Add New Task
Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs

✓ Task created successfully! (ID: 1)
  Title: Buy groceries
  Description: Milk, bread, eggs
```

## Error Handling

The application handles:
- ✅ Database connection errors
- ✅ Missing configuration
- ✅ Invalid input validation
- ✅ Task not found errors
- ✅ SQL transaction failures

## Development

### Running Tests

```bash
pytest tests/
```

### Adding New Features

1. Update domain entities if needed
2. Create/modify use cases in `application/use_cases/`
3. Implement in repository (both SQL and in-memory)
4. Update interactive interface

## Troubleshooting

### Database Connection Error
- Verify `.env` file exists and contains correct `PSQL_API` URL
- Check network connectivity to database
- Ensure database credentials are correct

### Import Errors
- Install all dependencies: `pip install -r requirements.txt`
- Verify Python version >= 3.13

### Table Not Found
- The app auto-creates tables on first run
- Check database permissions for table creation

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.

---

**Happy Task Managing! 🎯**
