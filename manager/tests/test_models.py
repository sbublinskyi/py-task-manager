import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from manager.models import Position, TaskType, Task


class ModelsTests(TestCase):
    def test_create_worker_with_position(self):
        position = Position.objects.create(name="QA")
        password = "user12345"

        worker = get_user_model().objects.create_user(
            username="test_user",
            first_name="Jason",
            last_name="Statham",
            password=password,
            position=position
        )

        self.assertEqual(
            str(worker),
            f"{worker.position.name}: {worker.first_name} "
            f"{worker.last_name} ({worker.username})"
        )
        self.assertTrue(worker.check_password(password))

    def test_create_worker_without_position(self):
        password = "user12345"

        worker = get_user_model().objects.create_user(
            username="test_user",
            first_name="Jason",
            last_name="Statham",
            password=password,
        )

        self.assertEqual(
            str(worker),
            f"No position: {worker.first_name} "
            f"{worker.last_name} ({worker.username})"
        )
        self.assertTrue(worker.check_password(password))

        self.assertEqual(worker.position, None)

    def test_position_str(self):
        name = "Developer"
        position = Position.objects.create(name=name)

        self.assertEqual(str(position), name)

    def test_task_type_str(self):
        name = "Bug"
        task_type = TaskType.objects.create(name=name)

        self.assertEqual(str(task_type), name)

    def test_task_str(self):
        task_type = TaskType.objects.create(name="bugfix")

        task = Task.objects.create(
            name="Problem",
            description="Everything is collapsed",
            deadline="2022-03-03 22:00:00",
            is_completed=False,
            priority="high",
            task_type=task_type,
        )

        self.assertEqual(
            str(task),
            f"Task: {task.name}, priority: {task.priority}, "
            f"deadline: {task.deadline} ({task.is_completed})"
        )
