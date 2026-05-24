from django.urls import path

from .views import login_user, register


urlpatterns = [
    path('register', register, name="user=register"),
    path('login', login_user, name="user-login")
]