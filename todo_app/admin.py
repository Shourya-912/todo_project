# todo_app/admin.py

from django.contrib import admin
from .models import Todo, Tag

admin.site.register(Todo)
admin.site.register(Tag)
