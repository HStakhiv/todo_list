from django.urls import path

from .views import (
    index,
    TaskCreateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TaskCreateView.as_view(), name="task-crate"),
    path("tags/create/", TagCreateView.as_view(), name="tag-crate"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
