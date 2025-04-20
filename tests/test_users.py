from fastapi import status


def test_create_user(client, db_session):
    """Test creating a new user."""
    user_data = {"name": "Alice", "is_manager": True}
    response = client.post("/users/", json=user_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "Alice"
    assert response.json()["is_manager"] is True


def test_get_users(client, db_session):
    """Test retrieving multiple users."""
    # Create test users
    client.post("/users/", json={"name": "Alice", "is_manager": True})
    client.post("/users/", json={"name": "Bob", "is_manager": False})

    response = client.get("/users/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == "Alice"
    assert response.json()[1]["name"] == "Bob"
