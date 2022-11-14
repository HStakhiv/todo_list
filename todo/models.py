from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField()
    tags = models.ManyToManyField(to=Tag, related_name="task")

    class Meta:
        ordering = ["status", "-datetime"]

    def __str__(self):
        return f"{self.content} {self.status}"
