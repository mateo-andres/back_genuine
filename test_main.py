from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from main import app

from config.db import get_db

client = TestClient(app)

# Create a global mock database
mock_db = MagicMock()

def override_get_db():
    try:
        yield mock_db
    finally:
        pass

app.dependency_overrides[get_db] = override_get_db


# ============ ROOT ENDPOINT TESTS ============
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# ============ STUDENTS ENDPOINT TESTS ============
def test_create_student():
    mock_db.reset_mock()
    
    student_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@test.com",
        "date_of_birth": "2000-01-15",
        "registration_date": "2024-01-01T00:00:00",
        "is_active": True
    }
    response = client.post("/students", json=student_data)
    assert response.status_code == 200
    assert response.json()["email"] == "john.doe@test.com"


def test_get_students():
    mock_db.reset_mock()
    mock_db.query.return_value.filter.return_value.all.return_value = []
    
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_student_by_id_not_found():
    mock_db.reset_mock()
    mock_db.query.return_value.filter.return_value.first.return_value = None
    
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


# ============ STAFF ENDPOINT TESTS ============
def test_create_staff():
    mock_db.reset_mock()
    
    staff_data = {
        "first_name": "Sarah",
        "last_name": "Smith",
        "email": "sarah.smith@test.com",
        "department": "teaching",
        "hire_date": "2024-01-01",
        "is_active": True
    }
    response = client.post("/staff", json=staff_data)
    assert response.status_code == 200
    assert response.json()["email"] == "sarah.smith@test.com"


def test_get_staff_unauthorized():
    response = client.get("/staff")
    assert response.status_code == 401


def test_get_staff_by_id_not_found():
    mock_db.reset_mock()
    mock_db.query.return_value.filter.return_value.first.return_value = None
    
    response = client.get("/staff/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Staff not found"}


# ============ TEACHERS ENDPOINT TESTS ============
def test_get_teachers():
    mock_db.reset_mock()
    # Configure the mock to return an empty list for the query chain
    mock_query = MagicMock()
    mock_filter = MagicMock()
    mock_filter.all.return_value = []
    mock_query.filter.return_value = mock_filter
    mock_db.query.return_value = mock_query
    
    response = client.get("/staff/teachers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json() == []
