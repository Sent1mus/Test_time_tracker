from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    """User model representing system users."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_manager = Column(Boolean, default=False)

    # Relationship to time entries
    time_entries = relationship("TimeEntry", back_populates="user")


class Project(Base):
    """Project model representing work projects."""

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Relationship to time entries
    time_entries = relationship("TimeEntry", back_populates="project")


class TimeEntry(Base):
    """Time entry model representing hours worked on projects."""

    __tablename__ = "time_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    date = Column(Date)
    hours = Column(Float)

    # Relationships to user and project
    user = relationship("User", back_populates="time_entries")
    project = relationship("Project", back_populates="time_entries")
