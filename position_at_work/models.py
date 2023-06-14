from django.db import models


class PositionAtWork(models.Model):

    title = models.CharField(
        verbose_name='Название',
        max_length=128,
        unique=True
    )

    class Meta:
        db_table = 'position_at_work'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности сотрудников'

    def __str__(self) -> str:
        return f'{self.title}'
