from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from manager.models import Position


class WorkerTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user_admin = get_user_model().objects.create_superuser(
            username="user_admin",
            password="superuser1234",
            position=Position.objects.create(name="QA")
        )

        self.client.force_login(self.user_admin)

    def test_position_listed(self):
        res = self.client.get(reverse("admin:manager_worker_changelist"))

        self.assertContains(res, self.user_admin.position)

    def test_position_change(self):
        res = self.client.get(
            reverse("admin:manager_worker_change", args=[self.user_admin.id])
        )

        self.assertContains(res, self.user_admin.position)

    def test_worker_fields_add(self):
        res = self.client.get(reverse("admin:manager_worker_add"))

        self.assertContains(res, "first_name")

        self.assertContains(res, "last_name")

        self.assertContains(res, "position")
