from fastapi.testclient import TestClient
from app.main import app
from app import models, crud
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, SessionLocal

# Создание тестовой базы данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionTestLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Настройка клиента
client = TestClient(app)

# Создание базы данных
def init_db():
    Base.metadata.create_all(bind=engine)

# Удаление базы данных
def drop_db():
    Base.metadata.drop_all(bind=engine)

# Тесты
def test_create_project():
    init_db()

    # Создаем проект
    response = client.post("/projects/", json={"name": "Project A"})
    assert response.status_code == 200
    assert response.json()["name"] == "Project A"

    drop_db()

def test_get_projects():
    init_db()

    # Создаем проекты
    client.post("/projects/", json={"name": "Project A"})
    client.post("/projects/", json={"name": "Project B"})

    # Проверяем список проектов
    response = client.get("/projects/")
    assert response.status_code == 200
    assert len(response.json()) == 2

    drop_db()
