from rest_framework import serializers

from atomic_habits.models import Habit
from atomic_habits.validators import EnjoyableValidator, NotEnjoyableValidator, CheckLinkedHabitValidator, \
    CheckTimeValidator, PatchEnjoyableValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
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
        validators = [EnjoyableValidator(fields=['is_enjoyable', 'linked_habit', 'reward']), NotEnjoyableValidator(fields=['is_enjoyable', 'linked_habit', 'reward']), CheckLinkedHabitValidator(field='linked_habit'), CheckTimeValidator(field='time')]

    def get_validators(self):
        """
        Determine the set of validators to use when instantiating serializer.
        """
        # If the validators have been declared explicitly then use that.
        if self.partial:
            enjoyable = self.context.get('is_enjoyable')
            linked_habit = self.context.get('linked_habit')
            reward = self.context.get('reward')
            if enjoyable is None and linked_habit is None and reward is None:
                validators = None
            elif enjoyable and linked_habit is None and reward is None:
                #need help
                print('here patch')
                list_validators = [PatchEnjoyableValidator]
                return list_validators
        else:
            validators = getattr(getattr(self, 'Meta', None), 'validators', None)
            if validators is not None:
                return list(validators)

        # Otherwise use the default set of validators.
        return (
                self.get_unique_together_validators() +
                self.get_unique_for_date_validators()
        )
