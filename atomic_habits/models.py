from django.conf import settings
from django.db import models
from django.utils.text import slugify

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    DAILY = 1
    IN_TWO = 2
    IN_THREE = 3
    IN_FOUR = 4
    IN_FIVE = 5
    IN_SIX = 6
    WEEKLY = 7

    PERIODICITY_CHOICES = [
        (DAILY, 'каждый день'),
        (IN_TWO, 'раз в два дня'),
        (IN_THREE, 'раз в три дня'),
        (IN_FOUR, 'раз в четыре дня'),
        (IN_FIVE, 'раз в пять дней'),
        (IN_SIX, 'раз в шесть дней'),
        (WEEKLY, 'раз в неделю')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=250, verbose_name='место')
    start_time = models.TimeField(verbose_name='время начала выполнения')
    action = models.CharField(max_length=250, verbose_name='действие')
    is_enjoyable = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    linked_habit = models.ForeignKey('self', unique=False, on_delete=models.CASCADE, **NULLABLE)
    periodicity = models.IntegerField(choices=PERIODICITY_CHOICES, default=DAILY, verbose_name='периодичность')
    reward = models.CharField(max_length=250, verbose_name='вознаграждение', **NULLABLE)
    time = models.PositiveIntegerField(verbose_name='время на выполнение привычки')
    is_public = models.BooleanField(default=False, verbose_name='признак публичной привычки')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'Я буду {self.action} в {self.start_time} в {self.place}'
