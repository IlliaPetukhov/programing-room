import random
from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import (
    Tasks,
    Programmer,
    LevelOfDifficulty,
    StatusOfTask,
)  # Замените 'catalog' на имя вашего приложения


class Command(BaseCommand):
    help = "Создать 200 задач"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Преобразуем QuerySet в списки для использования в random.choice()
        programmers = list(Programmer.objects.all())
        levels = list(LevelOfDifficulty.objects.all())
        statuses = list(StatusOfTask.objects.all())

        # Проверка наличия обязательных данных
        if not levels:
            self.stdout.write(self.style.ERROR("Нет уровней сложности в базе данных"))
            return

        if not statuses:
            self.stdout.write(self.style.ERROR("Нет статусов задач в базе данных"))
            return

        # Создание 200 задач
        for _ in range(200):
            chosen_status = random.choice(
                statuses
            )  # Выбор случайного объекта StatusOfTask

            if (
                chosen_status.status == "ready"
                or chosen_status.status == "somebody is doing this task"
            ):
                chosen_programmer = (
                    random.choice(programmers) if programmers else None
                )  # Выбор случайного программиста или None
            else:
                chosen_programmer = None

            chosen_level = random.choice(levels)  # Выбор случайного уровня сложности

            task = Tasks.objects.create(
                name=fake.sentence(nb_words=6),  # Генерация случайного названия задачи
                status=chosen_status,
                description=fake.paragraph(
                    nb_sentences=3
                ),  # Генерация случайного описания
                level=chosen_level,
                programmer=chosen_programmer,
            )

            # Вывод выбранных значений в консоль
            self.stdout.write(
                self.style.SUCCESS(f"Успешно создана задача: {task.name}\n")
            )
