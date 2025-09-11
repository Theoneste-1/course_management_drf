# Course Management API

## Overview

This is a Django REST Framework (DRF) backend API for a course management system. It allows users to create, manage, and enroll in courses, with support for modules and lessons. The API includes authentication, permissions for instructors, filtering, searching, ordering, and pagination.

The project is built with Django 5.2.3 and uses SQLite as the default database for development. It supports CRUD operations on courses, with read-only access for unauthenticated users and write access restricted to authenticated instructors.

## Features

- **Course Management**: Create, read, update, and delete courses with instructor assignment.
- **Nested Relationships**: Courses contain modules, which contain lessons (serialized read-only).
- **Enrollment System**: Enroll users in courses (with read-only student and enrollment date).
- **Authentication & Permissions**: Uses DRF's `IsAuthenticatedOrReadOnly` and custom `IsInstructorsOnly` permission. Token-based authentication.
- **Filtering & Searching**: Filter courses by instructor, search by title/description, and order results.
- **Pagination**: PageNumberPagination with configurable page size (default: 10).
- **API Root**: Provides links to `/courses/`, `/modules/`, `/lessons/`, and `/enrollments/`.

## Project Structure
course_manage/
├── course_manage/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── courses/  # Main app
│   ├── migrations/
│   ├── models.py  # Course, Module, Lesson, Enrollment
│   ├── serializers.py  # CourseSerializer, etc.
│   ├── views.py  # CourseViewSet
│   ├── permissions.py  # IsInstructorsOnly
│   └── urls.py
└── manage.py


## Models

- **Course**: Title, description, instructor (ForeignKey to User), created_at, updated_at.
- **Module**: Title, order (within course), related to Course.
- **Lesson**: Title, content, order (within module), related to Module.
- **Enrollment**: Student (ForeignKey to User), course, enrolled_at.

## Installation
1. **Clone the Repository**:
```markdown
git clone <your-repo-url>
cd course_manage</your-repo-url>
```


2. **Set Up Virtual Environment**:
```markdown
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**:
```
pip install -r requirements.txt
```

(Create `requirements.txt` if not present: `pip freeze > requirements.txt`. Key packages: `django==5.2.3`, `djangorestframework`, `djangorestframework-simplejwt` or token auth, `django-filter`.)

4. **Database Setup**:

```python manage.py makemigrations
python manage.py migrate
```


5. **Create Superuser** (for admin access):

```
python manage.py createsuperuser
```
- Username: e.g., "Theoneste" (admin and add to instructors group).

6. **Run the Development Server**:
```
python manage.py runserver
```

- Access the API at `http://localhost:8000/`.
- API root: `http://localhost:8000/` (provides endpoint links).
- Admin: `http://localhost:8000/admin/` (login with superuser).


## Usage

### Authentication
- Use token authentication. Obtain a token via login (e.g., using DRF's token endpoint or custom login view).
- Include in requests: `Authorization: Token <your-token>`.

### API Endpoints

Base URL: `http://localhost:8000/`

- **Courses** (`/courses/`):
  - **GET**: List all courses (paginated, filterable, searchable). Supports `?instructor=<username>`, `?search=<query>`, `?ordering=title`, `?page=2`.
  - **POST**: Create a course (authenticated instructor only). Example:
    ```json
    {
      "title": "Python Programming 101",
      "description": "An introductory course on Python programming."
    }