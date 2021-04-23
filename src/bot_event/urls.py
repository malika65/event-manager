from django.urls import path, include
from management.bot import webhook

urlpatterns = [
    path('', webhook)
]
