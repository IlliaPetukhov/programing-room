from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class LevelOfDifficulty(models.Model):
    level = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.level


class Programmer(AbstractUser):
    class Meta:
        verbose_name = "programmer"
        verbose_name_plural = "programmers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    # def get_absolute_url(self) -> dict:
    # return reverse("taxi:driver-detail", kwargs={"pk": self.pk})


class StatusOfTask(models.Model):
    status = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return self.status


class Tasks(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    status = models.ForeignKey(StatusOfTask, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    level = models.ForeignKey(
        LevelOfDifficulty, on_delete=models.CASCADE, null=False, blank=False
    )
    programmer = models.ForeignKey(
        Programmer, on_delete=models.CASCADE, null=True, blank=True
    )
