# Todo Project

This is a simple Django project for managing todos, providing a RESTful API for creating, updating, and deleting todos.

## Prerequisites

- Python 3.x
- Django
- Django Rest Framework

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/shourya-912/todo_project.git

2. Navigate to the project directory:
   
   `cd todo_project`
   
4. Install dependencies:

   `pip install -r requirements.txt`
   
5. Run migrations:
   `python manage.py migrate`
   
# Running the Development Server

Run the Django development server:
   `python manage.py runserver`

The application will be accessible at http://127.0.0.1:8000/.

# Running Tests

Run unit tests and integration tests:
   `python manage.py test todo_app.tests`

# Coverage Report
Generate a coverage report (assuming coverage is installed):
   `coverage run --source=todo_app manage.py test todo_app.tests`
   
   `coverage html`

The coverage report will be available in the htmlcov directory.

# Linting

Lint the code using flake8 and black:
  `flake8 .`
  
  ` black .`
   
# Github commands

Github commands to add, commit, and push the changes:
  `git add .`
  
  `git commit -m "Add GitHub Actions workflow for tests and linting"`
  
  `git push origin main`
  
You can write any other commit message instead of above message
