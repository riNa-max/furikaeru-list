from django.contrib import admin
from .models import TodoList,TodoStatus

# Register your models here.

admin.site.register(TodoList)
admin.site.register(TodoStatus)


