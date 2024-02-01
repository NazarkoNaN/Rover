from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser

from .models import MyUser
from .serializers import MyUserSerializer


# Create your views here.

class UserListAPIView(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

class UserAPIView(generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer