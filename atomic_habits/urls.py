from django.urls import path

from atomic_habits.apps import AtomicHabitsConfig
from atomic_habits.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    MyHabitListAPIView, HabitDestroyAPIView

app_name = AtomicHabitsConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habit_list'),
    path('my_habits/', MyHabitListAPIView.as_view(), name='my_habit_list'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habits/destroy/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_destroy'),
    ]
