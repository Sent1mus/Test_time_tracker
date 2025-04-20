from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """Create a new user in the database."""
    db_user = models.User(name=user.name, is_manager=user.is_manager)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> models.User | None:
    """Get a user by their ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    """Get a list of users with pagination."""
    return db.query(models.User).offset(skip).limit(limit).all()


def create_project(db: Session, project: schemas.ProjectCreate) -> models.Project:
    """Create a new project in the database."""
    db_project = models.Project(name=project.name)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_project(db: Session, project_id: int) -> models.Project | None:
    """Get a project by its ID."""
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100) -> list[models.Project]:
    """Get a list of projects with pagination."""
    return db.query(models.Project).offset(skip).limit(limit).all()


def create_time_entry(db: Session, time_entry: schemas.TimeEntryCreate) -> models.TimeEntry:
    """Create a new time entry in the database."""
    db_time_entry = models.TimeEntry(
        user_id=time_entry.user_id,
        project_id=time_entry.project_id,
        date=time_entry.date,
        hours=time_entry.hours
    )
    db.add(db_time_entry)
    db.commit()
    db.refresh(db_time_entry)
    return db_time_entry


def get_time_entries(
    db: Session, 
    user_id: int, 
    start_date: date, 
    end_date: date
) -> list[models.TimeEntry]:
    """Get time entries for a user within a date range."""
    return db.query(models.TimeEntry).filter(
        models.TimeEntry.user_id == user_id,
        models.TimeEntry.date >= start_date,
        models.TimeEntry.date < end_date
    ).all()


def get_report(
    db: Session, 
    project_id: int, 
    start_date: date, 
    end_date: date
) -> list[tuple[int, float]]:
    """Get a report of hours worked by users on a project within a date range."""
    return db.query(
        models.User.id,
        func.sum(models.TimeEntry.hours).label("hours")
    ).join(models.TimeEntry).filter(
        models.TimeEntry.project_id == project_id,
        models.TimeEntry.date >= start_date,
        models.TimeEntry.date < end_date
    ).group_by(models.User.id).all()