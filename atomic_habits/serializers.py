from rest_framework import serializers

from atomic_habits.models import Habit
from atomic_habits.validators import CheckLinkedHabitValidator, CheckTimeValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'pk',
            'place',
            'start_time',
            'action',
            'is_enjoyable',
            'linked_habit',
            'periodicity',
            'reward',
            'time',
            'is_public'
        )
        validators = [CheckLinkedHabitValidator(field='linked_habit'), CheckTimeValidator(field='time')]

    def validate(self, attrs):
        is_enjoyable, linked_habit, reward = attrs.get('is_enjoyable'), attrs.get('linked_habit'), attrs.get('reward')

        if self.context.get('request').method == 'PATCH':
            pk = self.context.get('request').path_info.split('/')[-2]
            habit = Habit.objects.get(pk=pk)

            is_enjoyable = habit.is_enjoyable if 'is_enjoyable' not in attrs else is_enjoyable
            linked_habit = habit.linked_habit.pk if 'linked_habit' not in attrs else linked_habit
            reward = habit.reward if 'reward' not in attrs else reward

        if is_enjoyable and reward:
            raise serializers.ValidationError('У приятной привычки не может быть награждения')
        elif is_enjoyable and linked_habit:
            raise serializers.ValidationError('У приятной привычки не может быть связанной приятной привычки')
        elif not is_enjoyable and not reward and not linked_habit:
            raise serializers.ValidationError('У полезной привычки должно быть награждение или связанная приятная привычка')
        elif not is_enjoyable and reward and linked_habit:
            raise serializers.ValidationError('Нельзя одновременно поощрить себя награждением и приятной привычкой')

        return attrs
