from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Tag, Task


def index(request):
    task = Task.objects.all()

    context = {
        "task": task,
    }

    return render(request, "todo/index.html", context)


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
