"""Database configuration module."""

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


def get_database_url() -> str:
    """Get database URL from environment variable.
    
    Returns:
        Database connection string
        
    Raises:
        ValueError: If PSQL_API environment variable is not set
    """
    db_url = os.getenv('PSQL_API')
    if not db_url:
        raise ValueError(
            "Database URL not found. Please set PSQL_API in .env file:\n"
            "PSQL_API=postgresql://user:password@host:port/database"
        )
    return db_url
