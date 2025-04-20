from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()


def get_db() -> Session:
    """Dependency for getting database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Project)
def create_project(
    project: schemas.ProjectCreate, db: Session = Depends(get_db)
) -> schemas.Project:
    """Create a new project."""
    return crud.create_project(db=db, project=project)


@router.get("/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)) -> schemas.Project:
    """Get a project by ID."""
    return crud.get_project(db=db, project_id=project_id)


@router.get("/", response_model=list[schemas.Project])
def read_projects(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> list[schemas.Project]:
    """Get a list of projects with pagination."""
    return crud.get_projects(db=db, skip=skip, limit=limit)
