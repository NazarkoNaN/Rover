from rest_framework import serializers
from django.contrib.auth.models import User

from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "date_joined"]


class MyUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MyUser
        fields = ["user", "photo", "city"]
