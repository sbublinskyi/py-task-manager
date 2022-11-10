import zoneinfo
from datetime import datetime

from django.db.models import QuerySet
from django.test import TestCase

from manager.forms import WorkerCreationForm, TaskForm, TaskSearchForm
from manager.models import Position, TaskType, Task


class FormsTests(TestCase):
    def test_worker_creation_form(self):
        position = Position.objects.create(name="QA")
        form_data = {
            "username": "test_user",
            "password1": "user1234",
            "password2": "user1234",
            "position": position,
            "first_name": "Jason",
            "last_name": "Statham"
        }

        form = WorkerCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_task_form(self):
        task_type = TaskType.objects.create(name="bug")
        form_data = {
            "name": "New bug",
            "description": "some description of a bug",
            "deadline": datetime(2022, 11, 11, 22, 0, tzinfo=zoneinfo.ZoneInfo(key='Europe/Kiev')),
            "is_completed": False,
            "priority": "high",
            "task_type": task_type,
        }

        form = TaskForm(data=form_data)

        self.assertTrue(form.is_valid())
