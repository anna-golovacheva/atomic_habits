from rest_framework import serializers

from atomic_habits.models import Habit


class EnjoyableValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        enjoyable = value.get('is_enjoyable')
        linked_habit = value.get('linked_habit')
        reward = value.get('reward')
        if enjoyable and reward:
            raise serializers.ValidationError('У приятной привычки не может быть награждения')
        elif enjoyable and linked_habit:
            raise serializers.ValidationError('У приятной привычки не может быть связанной приятной привычки')


class NotEnjoyableValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        enjoyable = value.get('is_enjoyable')
        linked_habit = value.get('linked_habit')
        reward = value.get('reward')
        if not enjoyable and not reward and not linked_habit:
            raise serializers.ValidationError('У полезной привычки должно быть награждение или связанная приятная привычка')
        elif not enjoyable and reward and linked_habit:
            raise serializers.ValidationError('Нельзя одновременно поощрить себя награждением и приятной привычкой')


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


class PatchEnjoyableValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        enjoyable = value.get('is_enjoyable')
        habit = Habit.objects.filter(pk=value.get('pk'))
        linked_habit = habit.linked_habit
        reward = habit.reward
        if enjoyable and reward:
            raise serializers.ValidationError('У приятной привычки не может быть награждения')
        elif enjoyable and linked_habit:
            raise serializers.ValidationError('У приятной привычки не может быть связанной приятной привычки')