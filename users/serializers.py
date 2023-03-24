from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'password', 'first_name', 'last_name', 'telegram_id')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], password=validated_data['password'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], telegram_id=validated_data['telegram_id'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )
