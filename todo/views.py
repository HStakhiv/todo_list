from django.shortcuts import render

from .models import Tag, Task


def index(request):
    task = Task.objects.all()

    context = {
        "task": task,
    }

    return render(request, "todo/index.html", context)
