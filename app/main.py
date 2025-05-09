from fastapi import FastAPI

from . import models
from .database import engine
from .routers import projects, time_entries, users

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title="Time Tracker API",
    description="API for tracking time spent on projects",
    version="1.0.0",
)

# Include routers with proper prefixes and tags
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(time_entries.router, prefix="/time-entries", tags=["time_entries"])
