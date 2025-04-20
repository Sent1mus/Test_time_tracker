# Указываем shell для Windows
set shell := ["powershell", "-NoProfile", "-Command"]

default:
    just up

up:
    docker-compose up --build

test:
    docker-compose run tests

lint:
    docker-compose exec app ruff check .
    docker-compose exec app black --check .

format:
    docker-compose exec app black .

install:
    pip install -r requirements.txt
