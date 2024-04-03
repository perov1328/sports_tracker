from django.db import models
from exercise.constants import EXERCISE_TYPE, DIFFICULTY_LEVEL


class Exercise(models.Model):
    """
    Модель для Упражнения
    """
    name = models.CharField(max_length=150, verbose_name='Название упражнения')
    description = models.TextField(verbose_name='Описание')
    exercise_type = models.CharField(max_length=20, choices=EXERCISE_TYPE, verbose_name='Тип упраженения')
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_LEVEL, verbose_name='Уровень сложности')
    duration = models.TimeField(verbose_name='Время на выполнение')
    approaches = models.IntegerField(verbose_name='Количество подходов')
    repetition = models.IntegerField(verbose_name='Количество повторений')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.exercise_type} - {self.name} ({self.difficulty_level})'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'
