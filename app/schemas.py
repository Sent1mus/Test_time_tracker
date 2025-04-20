from datetime import date

from pydantic import BaseModel


class UserBase(BaseModel):
    """Base schema for user data."""

    name: str
    is_manager: bool | None = False


class UserCreate(UserBase):
    """Schema for creating new users."""

    pass


class User(UserBase):
    """Schema for returning user data."""

    id: int

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    """Base schema for project data."""

    name: str


class ProjectCreate(ProjectBase):
    """Schema for creating new projects."""

    pass


class Project(ProjectBase):
    """Schema for returning project data."""

    id: int

    class Config:
        orm_mode = True


class TimeEntryBase(BaseModel):
    """Base schema for time entry data."""

    user_id: int
    project_id: int
    date: date
    hours: float


class TimeEntryCreate(TimeEntryBase):
    """Schema for creating new time entries."""

    pass


class TimeEntry(TimeEntryBase):
    """Schema for returning time entry data."""

    id: int

    class Config:
        orm_mode = True
