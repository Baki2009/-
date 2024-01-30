from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length = 100,
        verbose_name = "Заголовок"
    )
    description = models.TextField(
        verbose_name = "Описание"
    )
    completed = models.BooleanField(
        default = False,
        verbose_name = "Выполнено/Не выполнено"
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Дата и время создания"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список задач"
        verbose_name_plural = "Списки задач"