from django.urls import path

from .views import (
    register, confirm
)

app_name = 'auth'


urlpatterns = [
    path('auth/register', register, name="register"),
    path('auth/confirm', confirm, name="confirm"),
]
