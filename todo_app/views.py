from rest_framework import generics
from django.shortcuts import render
from .models import Tag, Todo
from .serializers import TodoSerializer
from django.views.generic import ListView, DetailView


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        todos = self.get_queryset()
        return render(request, "todo_app/todo_list.html", {"todos": todos})

    def create(self, request, *args, **kwargs):
        # Your existing logic for creating a Todo
        return super().create(request, *args, **kwargs)


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def retrieve(self, request, *args, **kwargs):
        todo = self.get_object()
        return render(request, "todo_app/todo_detail.html", {"todo": todo})

    def update(self, request, *args, **kwargs):
        # Your existing logic for updating a Todo
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Your existing logic for deleting a Todo
        return super().destroy(request, *args, **kwargs)


class TagListView(ListView):
    model = Tag
    template_name = "todo_app/tag_list.html"
    context_object_name = "tags"


class TagDetailView(DetailView):
    model = Tag
    template_name = "todo_app/tag_detail.html"
    context_object_name = "tag"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.filter(tags=self.object)
        return context
