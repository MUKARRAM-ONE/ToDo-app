# Research: Phase II Todo Full-Stack Web Application

## Decision: Frontend Framework - Next.js 16+ (App Router)
- **Rationale**: Core requirement of the constitution. Provides server-side rendering, efficient routing, and built-in support for server components which improves performance.
- **Alternatives Considered**: React (Vite) - Rejected due to lack of built-in SSR and App Router features.

## Decision: Backend Framework - FastAPI (Python 3.13+)
- **Rationale**: High performance, easy to use with async, and excellent support for Pydantic models which aligns with the constitution's requirement for strict validation.
- **Alternatives Considered**: Flask, Express.js - Rejected to stick with Python's high-performance FastAPI as per constitution.

## Decision: ORM - SQLModel
- **Rationale**: Combines SQLAlchemy and Pydantic, allowing for type-safe database models that double as validation schemas.
- **Alternatives Considered**: SQLAlchemy (standalone), Tortoise ORM - SQLModel is preferred for its seamless integration with FastAPI.

## Decision: Authentication - Better Auth + JWT
- **Rationale**: Better Auth provides a robust frontend auth experience, while JWT ensures a stateless backend as required by the constitution.
- **Alternatives Considered**: Session-based auth - Rejected per constitution's non-negotiable rule.

## Decision: Database - Neon PostgreSQL
- **Rationale**: Serverless PostgreSQL that scales well and is easy to integrate with serverless functions.
- **Alternatives Considered**: Local PostgreSQL, Supabase - Neon is the specified choice in the constitution.
