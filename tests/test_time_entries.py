import pytest
from fastapi import status
from datetime import date


def test_create_time_entry(client, db_session):
    """Test creating a new time entry."""
    # Setup required data
    user = client.post("/users/", json={"name": "Alice", "is_manager": True})
    project = client.post("/projects/", json={"name": "Project A"})

    time_entry_data = {
        "user_id": user.json()["id"],
        "project_id": project.json()["id"],
        "date": str(date.today()),
        "hours": 8.5
    }

    response = client.post("/time-entries/", json=time_entry_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["hours"] == 8.5


def test_get_time_entries(client, db_session):
    """Test retrieving time entries for a date range."""
    # Setup required data
    user = client.post("/users/", json={"name": "Alice", "is_manager": True})
    project = client.post("/projects/", json={"name": "Project A"})

    # Create test time entries
    client.post("/time-entries/", json={
        "user_id": user.json()["id"],
        "project_id": project.json()["id"],
        "date": "2023-01-01",
        "hours": 8
    })
    client.post("/time-entries/", json={
        "user_id": user.json()["id"],
        "project_id": project.json()["id"],
        "date": "2023-01-02",
        "hours": 7.5
    })

    response = client.get(
        "/time-entries/",
        params={
            "user_id": user.json()["id"],
            "start_date": "2023-01-01",
            "end_date": "2023-01-03"
        }
    )

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2