# Generated by Django 4.0.5 on 2024-06-23 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_tasks_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="programmer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.programmer",
            ),
        ),
    ]