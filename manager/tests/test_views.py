from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Task, TaskType, Position

HOME_PAGE_URL = reverse("manager:index")
TASK_LIST_URL = reverse("manager:task-list")
TASK_CREATE_URL = reverse("manager:task-create")
WORKER_LIST_URL = reverse("manager:worker-list")
WORKER_CREATE_URL = reverse("manager:worker-create")
TASK_TYPE_LIST_URL = reverse("manager:task-type-list")
TASK_TYPE_CREATE_URL = reverse("manager:task-type-create")
POSITION_LIST_URL = reverse("manager:position-list")
POSITION_CREATE_URL = reverse("manager:position-create")


class PublicPagesTests(TestCase):
    def test_home_page_login_required(self):
        res = self.client.get(HOME_PAGE_URL)

        self.assertEqual(res.status_code, 302)

    def test_task_list_login_required(self):
        res = self.client.get(TASK_LIST_URL)

        self.assertEqual(res.status_code, 302)

    def test_task_detail_login_required(self):
        task = Task.objects.create(
            name="Problem",
            description="Everything is collapsed",
            deadline="2022-03-03 22:00:00",
            is_completed=False,
            priority="high",
            task_type=TaskType.objects.create(name="bug"),
        )
        res = self.client.get(reverse("manager:task-detail", args=[task.id]))

        self.assertEqual(res.status_code, 302)

    def test_task_delete_login_required(self):
        task = Task.objects.create(
            name="Problem",
            description="Everything is collapsed",
            deadline="2022-03-03 22:00:00",
            is_completed=False,
            priority="high",
            task_type=TaskType.objects.create(name="bug"),
        )
        res = self.client.get(reverse("manager:task-delete", args=[task.id]))

        self.assertEqual(res.status_code, 302)

    def test_worker_list_login_required(self):
        res = self.client.get(WORKER_LIST_URL)

        self.assertEqual(res.status_code, 302)

    def test_task_worker_login_required(self):
        worker = get_user_model().objects.create_user(
            username="test_user",
            first_name="Jason",
            last_name="Statham",
            password="user12345",
            position=Position.objects.create(name="QA")
        )
        res = self.client.get(reverse("manager:worker-detail", args=[worker.id]))

        self.assertEqual(res.status_code, 302)

    def test_worker_delete_login_required(self):
        worker = get_user_model().objects.create_user(
            username="test_user",
            first_name="Jason",
            last_name="Statham",
            password="user12345",
            position=Position.objects.create(name="QA")
        )
        res = self.client.get(reverse("manager:worker-delete", args=[worker.id]))

        self.assertEqual(res.status_code, 302)

    def test_task_type_list_login_required(self):
        res = self.client.get(TASK_TYPE_LIST_URL)

        self.assertEqual(res.status_code, 302)

    def test_task_type_create_login_required(self):
        res = self.client.get(TASK_TYPE_CREATE_URL)

        self.assertEqual(res.status_code, 302)

    def test_task_type_delete_login_required(self):
        task_type = TaskType.objects.create(name="bug")
        res = self.client.get(reverse("manager:task-type-delete", args=[task_type.id]))

        self.assertEqual(res.status_code, 302)

    def test_position_list_login_required(self):
        res = self.client.get(POSITION_LIST_URL)

        self.assertEqual(res.status_code, 302)

    def test_position_create_login_required(self):
        res = self.client.get(POSITION_CREATE_URL)

        self.assertEqual(res.status_code, 302)

    def test_position_delete_login_required(self):
        position = TaskType.objects.create(name="QA")
        res = self.client.get(reverse("manager:position-delete", args=[position.id]))

        self.assertEqual(res.status_code, 302)
