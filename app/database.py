from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL (can be replaced with PostgreSQL)
DATABASE_URL = "sqlite:///./test.db"

# Create database engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # SQLite-specific parameter
)

# Session factory for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()
