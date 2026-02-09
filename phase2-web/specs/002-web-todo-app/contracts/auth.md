# API Contract: Authentication

## POST /api/auth/signup
- **Description**: Register a new user.
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword",
    "name": "John Doe"
  }
  ```
- **Success Response (201)**:
  ```json
  {
    "user": { "id": "uuid", "email": "user@example.com", "name": "John Doe" },
    "token": "jwt-token-string"
  }
  ```

## POST /api/auth/signin
- **Description**: Authenticate an existing user.
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```
- **Success Response (200)**:
  ```json
  {
    "user": { "id": "uuid", "email": "user@example.com", "name": "John Doe" },
    "token": "jwt-token-string"
  }
  ```

## POST /api/auth/signout
- **Description**: Clear the user session.
- **Request Body**: `{}`
- **Success Response (200)**:
  ```json
  { "success": true }
  ```
