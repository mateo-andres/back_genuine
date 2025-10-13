# Back Genuine - Educational Management System API

A RESTful API built with FastAPI for managing students, staff, and educational operations. This backend system provides comprehensive endpoints for educational institutions to manage their core operations including student enrollment, staff management, marketing, commercial activities, and metrics tracking.

## 🚀 Tech Stack

- **Framework**: FastAPI 0.119.0
- **Database**: PostgreSQL (via Railway)
- **ORM**: SQLAlchemy 2.0.44
- **Authentication**: JWT (JSON Web Tokens) with python-jose
- **Password Hashing**: Passlib with bcrypt
- **Validation**: Pydantic 2.12.0
- **Server**: Uvicorn 0.37.0
- **Testing**: Pytest 8.4.2
- **Python Version**: 3.12

## 📁 Project Structure

```
back_genuine/
├── config/
│   ├── auth.py              # JWT authentication & authorization logic
│   └── db.py                # Database connection & session management
├── models/
│   ├── staff.py             # Staff SQLAlchemy model & DepartmentEnum
│   └── students.py          # Student SQLAlchemy model
├── routes/
│   ├── commercial.py        # Commercial department endpoints
│   ├── marketing.py         # Marketing department endpoints
│   ├── metrics.py           # Metrics & analytics endpoints
│   ├── staff.py             # Staff CRUD operations
│   ├── students.py          # Student CRUD operations
│   └── teachers.py          # Teacher-specific endpoints
├── main.py                  # Application entry point & router configuration
├── schemas.py               # Pydantic models for request/response validation
├── requirements.txt         # Python dependencies
└── test_main.py             # API tests
```

## ✨ Features

### Core Functionality

- ✅ **Student Management**: Full CRUD operations for student records
- ✅ **Staff Management**: Employee records with department categorization
- ✅ **Authentication**: JWT-based authentication system
- ✅ **Role-Based Access**: Department-based authorization (teaching, commercial, marketing)
- ✅ **Soft Deletes**: Data preservation through is_active flags
- ✅ **CORS Support**: Configured for frontend integration
- ✅ **Metrics & Analytics**: Dedicated endpoints for tracking KPIs
- ✅ **Department-Specific Routes**: Specialized endpoints for each department

## 🗄️ Database Schema

### Students Table

```sql
- id: Integer (Primary Key, Auto-increment)
- first_name: String(100)
- last_name: String(100)
- email: String(255) [Unique, Indexed]
- date_of_birth: Date
- registration_date: DateTime [Default: now()]
- is_active: Boolean [Default: True]
```

### Staff Table

```sql
- id: Integer (Primary Key, Auto-increment)
- first_name: String(100)
- last_name: String(100)
- email: String(255) [Unique, Indexed]
- department: Enum(teaching, commercial, marketing)
- hire_date: Date [Default: now()]
- is_active: Boolean [Default: True]
```

## 🔌 API Endpoints

### Authentication

- `POST /login` - Authenticate user and receive JWT token

### Students

- `POST /students` - Create new student
- `GET /students` - List all active students
- `GET /students/{student_id}` - Get specific student
- `PUT /students/{student_id}` - Update student information
- `DELETE /students/{student_id}` - Soft delete student

### Staff

- `POST /staff` - Create new staff member
- `GET /staff` - List all active staff (requires authentication)
- `GET /staff/{staff_id}` - Get specific staff member
- `PUT /staff/{staff_id}` - Update staff information
- `DELETE /staff/{staff_id}` - Soft delete staff member

### Department-Specific Routes

- Teachers routes: `/teachers/*`
- Marketing routes: `/marketing/*`
- Commercial routes: `/commercial/*`
- Metrics routes: `/metrics/*`

## 🛠️ Setup and Installation

### Prerequisites

- Python 3.12+
- PostgreSQL database

### Installation Steps

1. **Create virtual environment**

```bash
python3 -m venv venv
```

2. **Activate virtual environment**

```bash
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Update dependencies (if needed)**

```bash
python -m pip freeze > requirements.txt
```

5. **Run the development server**

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Environment Variables

The application uses the following configuration (update in `config/db.py` for production):

- `DATABASE_URL`: PostgreSQL connection string
- `PORT`: Server port (default: 8000)

## 📖 Usage

### Interactive API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Authentication Flow

1. Call `POST /login` with email parameter
2. Receive JWT token in response
3. Include token in subsequent requests: `Authorization: Bearer <token>`

## 🔧 Configuration

### CORS Settings

The application is configured to accept requests from:

- `http://localhost:5173` (local development)
- `https://prueba-genuine.vercel.app` (production frontend)

Update the `origins` list in `main.py` to add more allowed origins.

## 🧪 Testing

Run tests using pytest:

```bash
pytest test_main.py
```
