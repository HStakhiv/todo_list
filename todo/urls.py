from django.urls import path

from .views import (
    index,
    TagListView,
    TagCreateView,
    TagUpdateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-crate"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update")
]

app_name = "todo"
