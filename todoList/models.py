from django.db import models
from django.utils import timezone

# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = ("Priority")
        verbose_name_plural = ("Priorities")


class State(models.Model):
    name = models.CharField(max_length=15)


class Todo(models.Model):
    description = models.CharField(max_length=150)
    priority = models.ForeignKey(Priority)
    state = models.ForeignKey(State) 
