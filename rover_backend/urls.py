from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path("users/", include("users.urls"), name="users"),

    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += staticfiles_urlpatterns()
