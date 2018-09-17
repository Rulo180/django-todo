from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Todo, State, Priority


def index(request): 
    todos = Todo.objects.all() 
    priorities = Priority.objects.all()
    states = State.objects.all()
    if request.method == 'POST':
        if "taskAdd" in request.POST:
            description = request.POST["description"]
            priority = request.POST["priority_select"]
            state = request.POST["state_select"]
            newTodo = Todo(description=description, priority=Priority.objects.get(name=priority), state=State.objects.get(name=state))
            newTodo.save()
            return redirect("/")
    if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = Todo.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, "index.html", {"todos": todos, "priorities":priorities, "states": states})
