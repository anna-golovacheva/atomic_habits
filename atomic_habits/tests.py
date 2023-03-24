from rest_framework.test import APITestCase
from rest_framework import status

from atomic_habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        test_email = 'test@te.ru'
        test_password = 'abc123'

        self.user = User(
            email=test_email,
            first_name='First',
            last_name='Last',
            telegram_id='123456789'
        )
        self.user.set_password(test_password)
        self.user.save()

        response = self.client.post(
            '/api/token/',
            {
                'email': test_email,
                'password': test_password
            }
        )
        self.access_token = response.json().get('access')

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_habit_create(self):
        self.test_model_place = "test place"
        self.test_model_start_time = "13:45:00"
        self.test_model_action = "test action"
        self.test_model_is_enjoyable = False
        self.test_model_linked_habit = None
        self.test_model_periodicity = 1
        self.test_model_reward = "test reward"
        self.test_model_time = 60
        self.test_model_is_public = True

        response = self.client.post(
            '/habits/create/',
            {
                "place": self.test_model_place,
                "start_time": self.test_model_start_time,
                "action": self.test_model_action,
                "is_enjoyable": self.test_model_is_enjoyable,
                "linked_habit": '',
                "periodicity": self.test_model_periodicity,
                "reward": self.test_model_reward,
                "time": self.test_model_time,
                "is_public": self.test_model_is_public

            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        test_habit = Habit.objects.first()
        self.test_model_pk = test_habit.pk

    def test_habit_retrieve(self):
        self.test_habit_create()
        response = self.client.get(
            f'/habits/{self.test_model_pk}/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "place": self.test_model_place,
                "start_time": self.test_model_start_time,
                "action": self.test_model_action,
                "is_enjoyable": self.test_model_is_enjoyable,
                "linked_habit": None,
                "periodicity": self.test_model_periodicity,
                "reward": self.test_model_reward,
                "time": self.test_model_time,
                "is_public": self.test_model_is_public
            }
        )

    def test_habit_list(self):
        self.test_habit_create()
        response = self.client.get(
            '/habits/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            [{
                "place": self.test_model_place,
                "start_time": self.test_model_start_time,
                "action": self.test_model_action,
                "is_enjoyable": self.test_model_is_enjoyable,
                "linked_habit": None,
                "periodicity": self.test_model_periodicity,
                "reward": self.test_model_reward,
                "time": self.test_model_time,
                "is_public": self.test_model_is_public
            }]
        )

    def test_habit_update(self):
        self.test_habit_create()
        self.test_model_updated_place = 'updated ' + self.test_model_place
        response = self.client.patch(
            f'/habits/update/{self.test_model_pk}/',
            {
                "place": self.test_model_updated_place,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "place": self.test_model_updated_place,
                "start_time": self.test_model_start_time,
                "action": self.test_model_action,
                "is_enjoyable": self.test_model_is_enjoyable,
                "linked_habit": None,
                "periodicity": self.test_model_periodicity,
                "reward": self.test_model_reward,
                "time": self.test_model_time,
                "is_public": self.test_model_is_public
            }
        )

    def test_habit_destroy(self):
        self.test_habit_create()
        response = self.client.delete(
            f'/habits/destroy/{self.test_model_pk}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
