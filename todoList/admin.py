from django.contrib import admin
from .models import Priority, State, Todo


# Register your models here.
admin.site.register(Priority)
admin.site.register(State)
admin.site.register(Todo)
