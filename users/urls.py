from users.apps import UsersConfig
from django.urls import path

from users.views import UserRetrieveAPIView, UserUpdateAPIView, RegisterApiView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    ]
