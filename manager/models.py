from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return (
            f"{self.position.name if self.position else 'No position'}: "
            f"{self.first_name} {self.last_name} ({self.username})"
        )


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return str(self.name)


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("highest", "Highest"),
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
        ("lowest", "Lowest"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField(default="2022-01-01")
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=63, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    def __str__(self) -> str:
        return (
            f"Task: {self.name}, priority: {self.priority}, "
            f"deadline: {self.deadline} ({self.is_completed})"
        )
