from django.urls import path

from .views import settings_post

urlpatterns = [
    path('', settings_post, name='settings'),
]
