from django.contrib.auth import login
from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from .models import MyUser
from .serializers import MyUserSerializer, MyUserRegisterSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class UserAPIView(generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class UserRegisterAPIView(generics.GenericAPIView):
    serializer_class = MyUserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        myUser = serializer.save()
        return Response({
            "user": MyUserSerializer(myUser).data,
            "token": AuthToken.objects.create(myUser.user)[1]
        })


class UserLoginAPIView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user.user)
        return super(UserLoginAPIView, self).post(request, format=None)
