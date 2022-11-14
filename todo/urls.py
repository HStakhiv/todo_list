from django.urls import path

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    toggle_for_tasks,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-crate"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path(
        "task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path("tags/create/", TagCreateView.as_view(), name="tag-crate"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/toggle/", toggle_for_tasks, name="toggle"),
]

app_name = "todo"
