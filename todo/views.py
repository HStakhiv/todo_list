from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def toggle_for_tasks(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = not task.status
    task.save()

    return HttpResponseRedirect(reverse_lazy("todo:index"))
