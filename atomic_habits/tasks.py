import datetime
import requests
from celery import shared_task
from django.conf import settings

from atomic_habits.models import Habit


@shared_task
def send_notifications():

    now_time = datetime.datetime.now().replace(second=0, microsecond=0)
    start_datetime = now_time + datetime.timedelta(minutes=5)

    upcoming_habits = Habit.objects.filter(start_time=start_datetime.time()).all()

    if upcoming_habits:

        for habit in upcoming_habits:
            telegram_id = habit.user.telegram_id
            action = habit.action
            place = habit.place

            resp = requests.get(f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={telegram_id}&text=Через 5 минут пора {action} в {place}').json()
            print(resp)
