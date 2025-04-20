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


@router.post("/", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate, db: Session = Depends(get_db)
) -> schemas.User:
    """Create a new user."""
    return crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)) -> schemas.User:
    """Get a user by ID."""
    return crud.get_user(db=db, user_id=user_id)


@router.get("/", response_model=list[schemas.User])
def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> list[schemas.User]:
    """Get a list of users with pagination."""
    return crud.get_users(db=db, skip=skip, limit=limit)
