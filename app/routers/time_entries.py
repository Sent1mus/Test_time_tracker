from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from .. import schemas, crud
from ..database import SessionLocal


router = APIRouter()


def get_db() -> Session:
    """Dependency for getting database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.TimeEntry)
def create_time_entry(
    time_entry: schemas.TimeEntryCreate,
    db: Session = Depends(get_db)
) -> schemas.TimeEntry:
    """Create a new time entry."""
    return crud.create_time_entry(db=db, time_entry=time_entry)


@router.get("/", response_model=list[schemas.TimeEntry])
def read_time_entries(
    user_id: int,
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
) -> list[schemas.TimeEntry]:
    """Get time entries for a user within a date range."""
    return crud.get_time_entries(
        db=db,
        user_id=user_id,
        start_date=start_date,
        end_date=end_date
    )


@router.get("/report", response_model=list[dict])
def get_report(
    project_id: int,
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
) -> list[dict]:
    """Get a report of hours worked by users on a project."""
    report = crud.get_report(
        db=db,
        project_id=project_id,
        start_date=start_date,
        end_date=end_date
    )
    return [{"id": user_id, "hours": hours} for user_id, hours in report]