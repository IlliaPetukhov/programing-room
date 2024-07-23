from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from django.test import TestCase
from django.urls import reverse
from catalog.models import Tasks, StatusOfTask, LevelOfDifficulty


class ViewTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="Gitarist2005",
            first_name="Test",
            last_name="Test",
        )
        self.level = LevelOfDifficulty.objects.create(level="easy")
        self.status = StatusOfTask.objects.create(status="you can take this task")
        StatusOfTask.objects.create(status="done")
        StatusOfTask.objects.create(status="somebody is doing this task")
        self.task = Tasks.objects.create(
            name="Test Task",
            description="Test Description",
            status=self.status,
            level=self.level,
            programmer=self.user,
        )
        self.client.force_login(self.user)

    def test_home_page_view(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "layouts/index.html")
        self.assertIn("num_programmers", response.context)
        self.assertIn("num_tasks", response.context)
        self.assertIn("num_visits", response.context)

    def test_page_list_of_tasks_view(self):
        response = self.client.get(reverse("catalog:about-us"))
        self.assertEqual(response.status_code, 200)

    def test_page_list_of_tasks_view_if_logged_out(self):
        self.client.logout()
        response = self.client.get(reverse("catalog:about-us"))
        self.assertNotEqual(response.status_code, 200)

    def test_page_my_tasks_view(self):
        response = self.client.get(reverse("catalog:my-task"))
        self.assertEqual(response.status_code, 200)

    def test_page_my_tasks_view_if_logged_out(self):
        self.client.logout()
        response = self.client.get(reverse("catalog:my-task"))
        self.assertNotEqual(response.status_code, 200)

    def test_page_all_tasks_if_admin_view(self):
        self.user.is_superuser = True
        self.user.save()
        response = self.client.get(reverse("catalog:tasks-if-admin"))
        self.assertEqual(response.status_code, 200)

    def test_page_all_tasks_if_not_admin_view(self):
        self.user.is_superuser = False
        self.user.save()
        response = self.client.get(reverse("catalog:tasks-if-admin"))
        self.assertNotEqual(response.status_code, 200)

    def test_change_status_if_tap_plus_or_done(self):
        if self.task.status.status == "you can take this task":
            self.client.post(
                reverse("catalog:change_task_status", kwargs={"pk": self.task.id})
            )
            self.task.refresh_from_db()
            self.assertEqual(self.task.status.status, "somebody is doing this task")

        if self.task.status.status == "somebody is doing this task":
            self.client.post(
                reverse("catalog:change_task_status", kwargs={"pk": self.task.id})
            )
            self.task.refresh_from_db()
            self.assertEqual(self.task.status.status, "done")
