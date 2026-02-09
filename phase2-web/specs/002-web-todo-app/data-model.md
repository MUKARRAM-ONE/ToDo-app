# Data Model: Phase II Todo App

## Entities

### User
- `id`: `String` (UUID, Primary Key) - Managed by Better Auth.
- `email`: `String` (Unique, Index)
- `name`: `String`
- `password_hash`: `String`
- `created_at`: `DateTime`
- `updated_at`: `DateTime`

### Task
- `id`: `Int` (Primary Key, Autoincrement)
- `user_id`: `String` (Foreign Key -> User.id, Index)
- `title`: `String` (Max 200 chars, Not Null)
- `description`: `String` (Optional)
- `completed`: `Boolean` (Default: False)
- `created_at`: `DateTime`
- `updated_at`: `DateTime`

## Relationships
- **User (1) <-> (*) Task**: A user can have multiple tasks. Each task belongs to exactly one user.
- **Cascading**: Deleting a user should delete all associated tasks.

## Validation Rules
- **Task Title**: Must not be empty.
- **User Email**: Must be a valid email format.
- **User Isolation**: Every query for tasks MUST include `user_id` filter.
