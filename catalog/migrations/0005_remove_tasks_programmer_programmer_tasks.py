# Generated by Django 4.0.5 on 2024-06-28 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_tasks_programmer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tasks",
            name="programmer",
        ),
        migrations.AddField(
            model_name="programmer",
            name="tasks",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.tasks",
            ),
        ),
    ]
