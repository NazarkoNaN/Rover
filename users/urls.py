from django.urls import path
from .views import *

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("<int:pk>/", UserAPIView.as_view(), name="user_retrieve"),
]
