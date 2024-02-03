from django.urls import path
from knox import views as knox_view
from .views import *

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),

    path("register/", UserRegisterAPIView.as_view(), name="user_create"),
    path("<int:pk>/", UserAPIView.as_view(), name="user_retrieve"),
    path("login/", UserLoginAPIView.as_view(), name="user_login"),
    path("logout/", knox_view.LogoutView.as_view(), name="user_logout"),
    path("logoutall/", knox_view.LogoutAllView.as_view(), name="user_logout_all"),
]
