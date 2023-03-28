from rest_framework import serializers
from atomic_habits.models import Habit


class CheckLinkedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        linked_habit = value.get('linked_habit')
        if linked_habit:
            habit = Habit.objects.filter(pk=linked_habit.pk).first()
            if habit:
                if not habit.is_enjoyable:
                    raise serializers.ValidationError('Связанная привычка должна быть приятной')


class CheckTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = value.get('time')
        if time:
            if time > 120:
                raise serializers.ValidationError('Время выполнения не может быть больше 120 секунд')
