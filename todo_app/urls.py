# todo_app/urls.py

from django.urls import path
from .views import (
    TodoListCreateView,
    TodoRetrieveUpdateDestroyView,
    TagListView,
    TagDetailView,
)

urlpatterns = [
    path("todos/", TodoListCreateView.as_view(), name="todo-list-create"),
    path(
        "todos/<int:pk>/",
        TodoRetrieveUpdateDestroyView.as_view(),
        name="todo-retrieve-update-destroy",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
]
