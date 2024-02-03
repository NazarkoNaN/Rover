from rest_framework import serializers
from django.contrib.auth.models import User

from .models import MyUser


# Default models.User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name",
                  "last_name", "email", "date_joined"]


# My custom MyUser serializer with nested defalt models.User serializer
class MyUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MyUser
        fields = "__all__"


# UserRegister serializer for MyUser serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]


# MyUser register serializer
class MyUserRegisterSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()

    class Meta:
        model = MyUser
        fields = ["user"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["user"]["username"], email=validated_data["user"]["email"], password=validated_data["user"]["password"])
        myUser = MyUser.objects.create(id=user.id, user=user)

        return myUser
