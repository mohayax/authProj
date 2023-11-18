from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up', views.signUP),
    path('users/<str:id>', views.getUsers),
    path('log-in', views.logIn),
    path('test-token', views.testToken),
]
