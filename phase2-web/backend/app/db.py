import os
from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine (using echo=True for debugging)
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    # This imports all models so they are registered with SQLModel.metadata
    from app.models import User, Task
    SQLModel.metadata.create_all(engine)
