from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    deadline = models.DateTimeField()
    status = models.BooleanField()
    tags = models.ManyToManyField(to=Tag, related_name="task")
