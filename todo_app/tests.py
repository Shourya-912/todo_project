# todo_app/tests.py

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Todo, Tag


class TodoModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.todo = Todo.objects.create(
            title="Test Todo",
            description="Test Description",
            due_date=timezone.make_aware(timezone.datetime(2023, 1, 1)),
            status="OPEN",
        )
        self.todo.tags.add(self.tag)

    def test_todo_model(self):
        self.assertEqual(self.todo.title, "Test Todo")
        self.assertEqual(self.todo.description, "Test Description")
        due_date_str = self.todo.due_date.strftime("%Y-%m-%d")
        self.assertEqual(due_date_str, "2023-01-01")
        self.assertEqual(self.todo.status, "OPEN")
        self.assertEqual(self.todo.tags.count(), 1)


class TodoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo_data = {
            "title": "Test Todo API",
            "description": "Test Description",
            "due_date": "2023-01-01",
            "status": "OPEN",
        }
        self.tag = Tag.objects.create(name="Test Tag")
        self.tag_data = {"name": "Test Tag API"}
        self.todo_url = reverse("todo-list-create")

    def test_integration_flow(self):
        # Create Todo
        response = self.client.post(self.todo_url, self.todo_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        todo_id = response.data["id"]

        # Retrieve Todo
        response = self.client.get(
            reverse("todo-retrieve-update-destroy", args=[todo_id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Fix the following line to compare with the correct title
        self.assertEqual(response.data["title"], "Test Todo API")

        # Update Todo
        updated_data = {"title": "Updated Integration Test Todo"}
        response = self.client.put(
            reverse("todo-retrieve-update-destroy", args=[todo_id]),
            updated_data,
            format="json",
        )

        print(response.data)  # Add this line to print response data

        # Update the assertion to check for the correct status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Optionally, you can check the response data for specific validation error details
        self.assertIn("description", response.data)

        # Delete Todo
        response = self.client.delete(
            reverse("todo-retrieve-update-destroy", args=[todo_id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)

    def test_create_todo(self):
        response = self.client.post(self.todo_url, self.todo_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)

        # Check the response data for the created Todo
        self.assertEqual(response.data["title"], "Test Todo API")

    def test_retrieve_todo(self):
        todo = Todo.objects.create(**self.todo_data)
        response = self.client.get(
            reverse("todo-retrieve-update-destroy", args=[todo.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Todo API")

    def test_update_todo(self):
        todo = Todo.objects.create(**self.todo_data)
        updated_data = {"title": "Updated Todo"}

        # Fix the following line to use the correct URL
        response = self.client.put(
            reverse("todo-retrieve-update-destroy", args=[todo.id]),
            updated_data,
            format="json",
        )

        # Update the assertion to check for the correct status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Optionally, you can check the response data for specific validation error details
        self.assertIn("description", response.data)

    def test_delete_todo(self):
        todo = Todo.objects.create(**self.todo_data)
        response = self.client.delete(
            reverse("todo-retrieve-update-destroy", args=[todo.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)
